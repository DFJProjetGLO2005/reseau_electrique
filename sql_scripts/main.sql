
SET FOREIGN_KEY_CHECKS=0;
source A_Init.sql
source B_CreateTables.sql
source C_PrimaryKeys.sql
source D_ForeignKeys.sql
source E_Triggers.sql
source F_InsertInto.sql
source G_Indexes.sql
SET FOREIGN_KEY_CHECKS=1;
SELECT "L'installation a reussi." as "";

