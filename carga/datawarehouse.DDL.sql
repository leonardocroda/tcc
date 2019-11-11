CREATE TABLE IF NOT EXISTS DimFeeling (
  idDimFeeling INT NOT NULL,
  feeling VARCHAR(45) NOT NULL,
  PRIMARY KEY (idDimFeeling)
);

CREATE TABLE IF NOT EXISTS DimTime (
  idDimTime INT NOT NULL,
  day INT NULL,
  mounth INT NULL,
  year INT NULL,
  hour DATETIME NULL,
  shift VARCHAR(45) NULL,
  season VARCHAR(45) NULL,
  PRIMARY KEY (idDimTime)
);

CREATE TABLE IF NOT EXISTS DimCharacteristics (
  idDimCharacteristics INT NOT NULL,
  characteristic VARCHAR(45) NOT NULL,
  PRIMARY KEY (idDimCharacteristics)
);

CREATE TABLE IF NOT EXISTS DimText (
  idDimText INT NOT NULL,
  text VARCHAR(280) NULL,
  PRIMARY KEY (idDimText)
);

CREATE TABLE IF NOT EXISTS FactTweet (
  idFactTweet INT NOT NULL,
  DimCharacteristics_idDimCharacteristics INT REFERENCES DimCharacteristics (idDimCharacteristics),
  DimFeeling_idDimFeeling INT REFERENCES DimFeeling (idDimFeeling),
  DimText_idDimText INT REFERENCES DimText (idDimText),
  DimTime_idDimTime INT REFERENCES DimTime (idDimTime),
  PRIMARY KEY (idFactTweet)
);
