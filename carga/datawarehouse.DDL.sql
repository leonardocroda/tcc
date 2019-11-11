CREATE TABLE IF NOT EXISTS DimFeeling (
  idDimFeeling INT NOT NULL,
  feeling VARCHAR(45) NOT NULL,
  PRIMARY KEY (idDimFeeling)
);

CREATE TABLE IF NOT EXISTS DimTime (
  idDimTime BIGINT,
  day INT,
  month VARCHAR(4),
  year INT,
  dayweek VARCHAR(45),
  hour VARCHAR (8),
  shift VARCHAR(45),
  PRIMARY KEY (idDimTime)
);

CREATE TABLE IF NOT EXISTS DimCharacteristics (
  idDimCharacteristics CHAR NOT NULL,
  characteristic VARCHAR(45) NOT NULL,
  PRIMARY KEY (idDimCharacteristics)
);

CREATE TABLE IF NOT EXISTS DimText (
  idDimText BIGINT,
  text VARCHAR(2000) NULL,
  PRIMARY KEY (idDimText)
);

CREATE TABLE IF NOT EXISTS FactTweet (
  idFactTweet SERIAL,
  characteristics CHAR REFERENCES DimCharacteristics (idDimCharacteristics),
  feeling INT REFERENCES DimFeeling (idDimFeeling),
  text BIGINT REFERENCES DimText (idDimText),
  time BIGINT REFERENCES DimTime (idDimTime),
  PRIMARY KEY (idFactTweet)
);
