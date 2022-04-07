import pandas
import savReaderWriter

with savReaderWriter.SavReader('ATP W63.sav', returnHeader=True) as reader:
    df = pandas.DataFrame(reader.all())

    print(df.head())
    print(df.shape)
    df.to_csv('ATP W63.txt', sep="|", index=False)



