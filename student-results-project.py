import pandas as pd

data = {
    "name":["praful","amit","raj","vishal","riya","jay"],
    "math":[85,92,45,78,55,90],
    "science":[78,88,50,82,60,95],
    "english":[70,85,40,75,65,88],
    "city":["mumbai","delhi","pune","mumbai","delhi","pune"]
}

df = pd.DataFrame(data)

print("===student data===")
print(df)


df["total"] =df["math"] = df["science"] = df["english"]

df["percentage"] = (df["total"]/300) *100

df["grade"] = df["percentage"].apply(lambda x:"A" if x >= 80 else ("B" if x >= 60 else "C"))

df["result"] = df["percentage"].apply(lambda x : "pass" if x>= 40 else "fail")

print("\n===topper===")
print(df.nlargest(1,"percentage")[["name","percentage"]])


print("\n===city wise average ===")
print(df.groupby("city")["percentage"].mean())

print("\n===grade count ===")
print(df["grade"].value_counts())

print("\n=== Ranking ===")
df["rank"] = df["total"].rank(ascending=False).astype(int)
print(df[["name","total","percentage","grade","rank"]])

df.to_csv("student_result.csv", index=False)
print("\nCSV save ho gayi!")
