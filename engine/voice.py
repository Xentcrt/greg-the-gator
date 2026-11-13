# Joins Greg's sentences into one track and writes timing.json (sentence, word and mouth timing).
import json, re, numpy as np, soundfile as sf
import sys, os
# usage: python3 voice.py EPISODE_DIR WORK_DIR  (WORK_DIR/voice/<id>_<n>.wav must exist)
EP=os.path.abspath(sys.argv[1])+'/'; P=os.path.abspath(sys.argv[2])+'/'
os.makedirs(P+'assets',exist_ok=True)
S=json.load(open(EP+'script.json'))
SR=24000; FPS=30
LEAD=0.40; GAP_IN=0.18; GAP_SEC=0.45; TAIL=1.3
def trim(x):
    env=np.abs(x); thr=max(env.max()*0.02,1e-4)
    idx=np.where(env>thr)[0]
    a=max(idx[0]-int(0.02*SR),0); b=min(idx[-1]+int(0.06*SR),len(x))
    y=x[a:b].copy()
    f=int(0.008*SR); y[:f]*=np.linspace(0,1,f); y[-f:]*=np.linspace(1,0,f)
    return y
def syl(w):
    w=re.sub(r"[^a-z]","",w.lower())
    n=len(re.findall(r"[aeiouy]+",w))
    if w.endswith('e') and n>1 and not w.endswith('le'): n-=1
    return max(n,1)
out=[np.zeros(int(LEAD*SR),np.float32)]; t=LEAD; secs=[]
for si,sec in enumerate(S):
    s={'id':sec['id'],'start':t,'sentences':[]}
    for i,line in enumerate(sec['lines']):
        x,sr=sf.read(f"{P}voice/{sec['id']}_{i}.wav",dtype='float32'); assert sr==SR
        if x.ndim>1: x=x.mean(1)
        x=trim(x); d=len(x)/SR
        words=line.split()
        w=[syl(k)+0.45+(0.5 if re.search(r"[,:]$",k) else 0) for k in words]
        tot=sum(w); acc=0; ws=[]
        for k,wk in zip(words,w):
            a=t+0.03+(d-0.09)*acc/tot; acc+=wk; b=t+0.03+(d-0.09)*acc/tot
            ws.append({'w':k,'s':round(a,3),'e':round(b,3)})
        s['sentences'].append({'text':line,'s':round(t,3),'e':round(t+d,3),'words':ws})
        out.append(x); t+=d
        last=(i==len(sec['lines'])-1)
        g=GAP_SEC if last else GAP_IN
        if not (last and si==len(S)-1):
            out.append(np.zeros(int(g*SR),np.float32)); t+=int(g*SR)/SR
    s['end']=s['sentences'][-1]['e']; secs.append(s)
out.append(np.zeros(int(TAIL*SR),np.float32))
y=np.concatenate(out); pk=np.abs(y).max(); y=y/pk*0.89
# whole number of frames
n=int(np.ceil(len(y)/SR*FPS)); y=np.pad(y,(0,n*SR//FPS-len(y)))
sf.write(P+'assets/greg-voice.wav',y,SR,subtype='PCM_16')
# mouth: loudness per frame -> 0..1
hop=SR//FPS; rms=np.array([np.sqrt(np.mean(y[i*hop:(i+1)*hop]**2)+1e-12) for i in range(n)])
m=np.clip(rms/np.percentile(rms[rms>0.01],85),0,1)**0.7
m[m<0.12]=0
sm=np.copy(m)
for i in range(1,n): sm[i]=max(m[i],sm[i-1]*0.55) if m[i]>0 else sm[i-1]*0.45
sm[sm<0.04]=0
json.dump({'duration':n/FPS,'fps':FPS,'sections':secs,'mouth':[round(float(v),2) for v in sm]},open(P+'timing.json','w'),indent=1)
print('duration',n/FPS)
for s in secs: print(s['id'],round(s['start'],2),round(s['end'],2))
