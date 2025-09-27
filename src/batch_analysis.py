import os,json,pandas as pd
def summarize(results_dir="results"):
    rows=[]
    for f in os.listdir(results_dir):
        if f.endswith(".json"):
            data=json.load(open(os.path.join(results_dir,f)))
            rows.append({"task":data["task"],"model":data["model"],"steps":data["steps"],"achieved":data["achieved"],"reward":data["reward"],"safety":data.get("safety_flag","")})
    df=pd.DataFrame(rows); print(df.groupby("model")[["reward","achieved","steps"]].mean()); return df
if __name__=="__main__": summarize()
