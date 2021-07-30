BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "eveng" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT,
	"ip_addr"	TEXT,
	"device_type"	TEXT,
	"username"	TEXT,
	"password"	TEXT,
	"location"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "eveng" VALUES (1,'R1','10.0.1.1','router','cisco','cisco','lab');
INSERT INTO "eveng" VALUES (2,'R2','10.0.1.2','router','cisco','cisco','lab');
INSERT INTO "eveng" VALUES (3,'S1','10.0.1.201','switch','cisco','cisco','lab');
INSERT INTO "eveng" VALUES (4,'S2','10.0.1.202','switch','cisco','cisco','lab');
INSERT INTO "eveng" VALUES (5,'S3','10.0.1.203','switch','cisco','cisco','lab');
INSERT INTO "eveng" VALUES (6,'S4','10.0.1.204','switch','cisco','cisco','lab');
INSERT INTO "eveng" VALUES (7,'S5','10.0.1.205','switch','cisco','cisco','lab');
INSERT INTO "eveng" VALUES (8,'S6','10.0.1.206','switch','cisco','cisco','lab');
COMMIT;
