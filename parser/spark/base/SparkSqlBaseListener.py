# Generated from SparkSqlBase.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SparkSqlBaseParser import SparkSqlBaseParser
else:
    from SparkSqlBaseParser import SparkSqlBaseParser

# This class defines a complete listener for a parse tree produced by SparkSqlBaseParser.
class SparkSqlBaseListener(ParseTreeListener):

    # Enter a parse tree produced by SparkSqlBaseParser#singleStatement.
    def enterSingleStatement(self, ctx:SparkSqlBaseParser.SingleStatementContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#singleStatement.
    def exitSingleStatement(self, ctx:SparkSqlBaseParser.SingleStatementContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#singleExpression.
    def enterSingleExpression(self, ctx:SparkSqlBaseParser.SingleExpressionContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#singleExpression.
    def exitSingleExpression(self, ctx:SparkSqlBaseParser.SingleExpressionContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#singleTableIdentifier.
    def enterSingleTableIdentifier(self, ctx:SparkSqlBaseParser.SingleTableIdentifierContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#singleTableIdentifier.
    def exitSingleTableIdentifier(self, ctx:SparkSqlBaseParser.SingleTableIdentifierContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#singleFunctionIdentifier.
    def enterSingleFunctionIdentifier(self, ctx:SparkSqlBaseParser.SingleFunctionIdentifierContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#singleFunctionIdentifier.
    def exitSingleFunctionIdentifier(self, ctx:SparkSqlBaseParser.SingleFunctionIdentifierContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#singleDataType.
    def enterSingleDataType(self, ctx:SparkSqlBaseParser.SingleDataTypeContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#singleDataType.
    def exitSingleDataType(self, ctx:SparkSqlBaseParser.SingleDataTypeContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#singleTableSchema.
    def enterSingleTableSchema(self, ctx:SparkSqlBaseParser.SingleTableSchemaContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#singleTableSchema.
    def exitSingleTableSchema(self, ctx:SparkSqlBaseParser.SingleTableSchemaContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#statementDefault.
    def enterStatementDefault(self, ctx:SparkSqlBaseParser.StatementDefaultContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#statementDefault.
    def exitStatementDefault(self, ctx:SparkSqlBaseParser.StatementDefaultContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#use.
    def enterUse(self, ctx:SparkSqlBaseParser.UseContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#use.
    def exitUse(self, ctx:SparkSqlBaseParser.UseContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#createDatabase.
    def enterCreateDatabase(self, ctx:SparkSqlBaseParser.CreateDatabaseContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#createDatabase.
    def exitCreateDatabase(self, ctx:SparkSqlBaseParser.CreateDatabaseContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#setDatabaseProperties.
    def enterSetDatabaseProperties(self, ctx:SparkSqlBaseParser.SetDatabasePropertiesContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#setDatabaseProperties.
    def exitSetDatabaseProperties(self, ctx:SparkSqlBaseParser.SetDatabasePropertiesContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#dropDatabase.
    def enterDropDatabase(self, ctx:SparkSqlBaseParser.DropDatabaseContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#dropDatabase.
    def exitDropDatabase(self, ctx:SparkSqlBaseParser.DropDatabaseContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#createTable.
    def enterCreateTable(self, ctx:SparkSqlBaseParser.CreateTableContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#createTable.
    def exitCreateTable(self, ctx:SparkSqlBaseParser.CreateTableContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#createHiveTable.
    def enterCreateHiveTable(self, ctx:SparkSqlBaseParser.CreateHiveTableContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#createHiveTable.
    def exitCreateHiveTable(self, ctx:SparkSqlBaseParser.CreateHiveTableContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#createTableLike.
    def enterCreateTableLike(self, ctx:SparkSqlBaseParser.CreateTableLikeContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#createTableLike.
    def exitCreateTableLike(self, ctx:SparkSqlBaseParser.CreateTableLikeContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#analyze.
    def enterAnalyze(self, ctx:SparkSqlBaseParser.AnalyzeContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#analyze.
    def exitAnalyze(self, ctx:SparkSqlBaseParser.AnalyzeContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#addTableColumns.
    def enterAddTableColumns(self, ctx:SparkSqlBaseParser.AddTableColumnsContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#addTableColumns.
    def exitAddTableColumns(self, ctx:SparkSqlBaseParser.AddTableColumnsContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#renameTable.
    def enterRenameTable(self, ctx:SparkSqlBaseParser.RenameTableContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#renameTable.
    def exitRenameTable(self, ctx:SparkSqlBaseParser.RenameTableContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#setTableProperties.
    def enterSetTableProperties(self, ctx:SparkSqlBaseParser.SetTablePropertiesContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#setTableProperties.
    def exitSetTableProperties(self, ctx:SparkSqlBaseParser.SetTablePropertiesContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#unsetTableProperties.
    def enterUnsetTableProperties(self, ctx:SparkSqlBaseParser.UnsetTablePropertiesContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#unsetTableProperties.
    def exitUnsetTableProperties(self, ctx:SparkSqlBaseParser.UnsetTablePropertiesContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#changeColumn.
    def enterChangeColumn(self, ctx:SparkSqlBaseParser.ChangeColumnContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#changeColumn.
    def exitChangeColumn(self, ctx:SparkSqlBaseParser.ChangeColumnContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#setTableSerDe.
    def enterSetTableSerDe(self, ctx:SparkSqlBaseParser.SetTableSerDeContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#setTableSerDe.
    def exitSetTableSerDe(self, ctx:SparkSqlBaseParser.SetTableSerDeContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#addTablePartition.
    def enterAddTablePartition(self, ctx:SparkSqlBaseParser.AddTablePartitionContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#addTablePartition.
    def exitAddTablePartition(self, ctx:SparkSqlBaseParser.AddTablePartitionContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#renameTablePartition.
    def enterRenameTablePartition(self, ctx:SparkSqlBaseParser.RenameTablePartitionContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#renameTablePartition.
    def exitRenameTablePartition(self, ctx:SparkSqlBaseParser.RenameTablePartitionContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#dropTablePartitions.
    def enterDropTablePartitions(self, ctx:SparkSqlBaseParser.DropTablePartitionsContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#dropTablePartitions.
    def exitDropTablePartitions(self, ctx:SparkSqlBaseParser.DropTablePartitionsContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#setTableLocation.
    def enterSetTableLocation(self, ctx:SparkSqlBaseParser.SetTableLocationContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#setTableLocation.
    def exitSetTableLocation(self, ctx:SparkSqlBaseParser.SetTableLocationContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#recoverPartitions.
    def enterRecoverPartitions(self, ctx:SparkSqlBaseParser.RecoverPartitionsContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#recoverPartitions.
    def exitRecoverPartitions(self, ctx:SparkSqlBaseParser.RecoverPartitionsContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#dropTable.
    def enterDropTable(self, ctx:SparkSqlBaseParser.DropTableContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#dropTable.
    def exitDropTable(self, ctx:SparkSqlBaseParser.DropTableContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#createView.
    def enterCreateView(self, ctx:SparkSqlBaseParser.CreateViewContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#createView.
    def exitCreateView(self, ctx:SparkSqlBaseParser.CreateViewContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#createTempViewUsing.
    def enterCreateTempViewUsing(self, ctx:SparkSqlBaseParser.CreateTempViewUsingContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#createTempViewUsing.
    def exitCreateTempViewUsing(self, ctx:SparkSqlBaseParser.CreateTempViewUsingContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#alterViewQuery.
    def enterAlterViewQuery(self, ctx:SparkSqlBaseParser.AlterViewQueryContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#alterViewQuery.
    def exitAlterViewQuery(self, ctx:SparkSqlBaseParser.AlterViewQueryContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#createFunction.
    def enterCreateFunction(self, ctx:SparkSqlBaseParser.CreateFunctionContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#createFunction.
    def exitCreateFunction(self, ctx:SparkSqlBaseParser.CreateFunctionContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#dropFunction.
    def enterDropFunction(self, ctx:SparkSqlBaseParser.DropFunctionContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#dropFunction.
    def exitDropFunction(self, ctx:SparkSqlBaseParser.DropFunctionContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#explain.
    def enterExplain(self, ctx:SparkSqlBaseParser.ExplainContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#explain.
    def exitExplain(self, ctx:SparkSqlBaseParser.ExplainContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#showTables.
    def enterShowTables(self, ctx:SparkSqlBaseParser.ShowTablesContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#showTables.
    def exitShowTables(self, ctx:SparkSqlBaseParser.ShowTablesContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#showTable.
    def enterShowTable(self, ctx:SparkSqlBaseParser.ShowTableContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#showTable.
    def exitShowTable(self, ctx:SparkSqlBaseParser.ShowTableContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#showDatabases.
    def enterShowDatabases(self, ctx:SparkSqlBaseParser.ShowDatabasesContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#showDatabases.
    def exitShowDatabases(self, ctx:SparkSqlBaseParser.ShowDatabasesContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#showTblProperties.
    def enterShowTblProperties(self, ctx:SparkSqlBaseParser.ShowTblPropertiesContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#showTblProperties.
    def exitShowTblProperties(self, ctx:SparkSqlBaseParser.ShowTblPropertiesContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#showColumns.
    def enterShowColumns(self, ctx:SparkSqlBaseParser.ShowColumnsContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#showColumns.
    def exitShowColumns(self, ctx:SparkSqlBaseParser.ShowColumnsContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#showPartitions.
    def enterShowPartitions(self, ctx:SparkSqlBaseParser.ShowPartitionsContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#showPartitions.
    def exitShowPartitions(self, ctx:SparkSqlBaseParser.ShowPartitionsContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#showFunctions.
    def enterShowFunctions(self, ctx:SparkSqlBaseParser.ShowFunctionsContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#showFunctions.
    def exitShowFunctions(self, ctx:SparkSqlBaseParser.ShowFunctionsContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#showCreateTable.
    def enterShowCreateTable(self, ctx:SparkSqlBaseParser.ShowCreateTableContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#showCreateTable.
    def exitShowCreateTable(self, ctx:SparkSqlBaseParser.ShowCreateTableContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#describeFunction.
    def enterDescribeFunction(self, ctx:SparkSqlBaseParser.DescribeFunctionContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#describeFunction.
    def exitDescribeFunction(self, ctx:SparkSqlBaseParser.DescribeFunctionContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#describeDatabase.
    def enterDescribeDatabase(self, ctx:SparkSqlBaseParser.DescribeDatabaseContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#describeDatabase.
    def exitDescribeDatabase(self, ctx:SparkSqlBaseParser.DescribeDatabaseContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#describeTable.
    def enterDescribeTable(self, ctx:SparkSqlBaseParser.DescribeTableContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#describeTable.
    def exitDescribeTable(self, ctx:SparkSqlBaseParser.DescribeTableContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#refreshTable.
    def enterRefreshTable(self, ctx:SparkSqlBaseParser.RefreshTableContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#refreshTable.
    def exitRefreshTable(self, ctx:SparkSqlBaseParser.RefreshTableContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#refreshResource.
    def enterRefreshResource(self, ctx:SparkSqlBaseParser.RefreshResourceContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#refreshResource.
    def exitRefreshResource(self, ctx:SparkSqlBaseParser.RefreshResourceContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#cacheTable.
    def enterCacheTable(self, ctx:SparkSqlBaseParser.CacheTableContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#cacheTable.
    def exitCacheTable(self, ctx:SparkSqlBaseParser.CacheTableContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#uncacheTable.
    def enterUncacheTable(self, ctx:SparkSqlBaseParser.UncacheTableContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#uncacheTable.
    def exitUncacheTable(self, ctx:SparkSqlBaseParser.UncacheTableContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#clearCache.
    def enterClearCache(self, ctx:SparkSqlBaseParser.ClearCacheContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#clearCache.
    def exitClearCache(self, ctx:SparkSqlBaseParser.ClearCacheContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#loadData.
    def enterLoadData(self, ctx:SparkSqlBaseParser.LoadDataContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#loadData.
    def exitLoadData(self, ctx:SparkSqlBaseParser.LoadDataContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#truncateTable.
    def enterTruncateTable(self, ctx:SparkSqlBaseParser.TruncateTableContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#truncateTable.
    def exitTruncateTable(self, ctx:SparkSqlBaseParser.TruncateTableContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#repairTable.
    def enterRepairTable(self, ctx:SparkSqlBaseParser.RepairTableContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#repairTable.
    def exitRepairTable(self, ctx:SparkSqlBaseParser.RepairTableContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#manageResource.
    def enterManageResource(self, ctx:SparkSqlBaseParser.ManageResourceContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#manageResource.
    def exitManageResource(self, ctx:SparkSqlBaseParser.ManageResourceContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#failNativeCommand.
    def enterFailNativeCommand(self, ctx:SparkSqlBaseParser.FailNativeCommandContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#failNativeCommand.
    def exitFailNativeCommand(self, ctx:SparkSqlBaseParser.FailNativeCommandContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#setConfiguration.
    def enterSetConfiguration(self, ctx:SparkSqlBaseParser.SetConfigurationContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#setConfiguration.
    def exitSetConfiguration(self, ctx:SparkSqlBaseParser.SetConfigurationContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#resetConfiguration.
    def enterResetConfiguration(self, ctx:SparkSqlBaseParser.ResetConfigurationContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#resetConfiguration.
    def exitResetConfiguration(self, ctx:SparkSqlBaseParser.ResetConfigurationContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#unsupportedHiveNativeCommands.
    def enterUnsupportedHiveNativeCommands(self, ctx:SparkSqlBaseParser.UnsupportedHiveNativeCommandsContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#unsupportedHiveNativeCommands.
    def exitUnsupportedHiveNativeCommands(self, ctx:SparkSqlBaseParser.UnsupportedHiveNativeCommandsContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#createTableHeader.
    def enterCreateTableHeader(self, ctx:SparkSqlBaseParser.CreateTableHeaderContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#createTableHeader.
    def exitCreateTableHeader(self, ctx:SparkSqlBaseParser.CreateTableHeaderContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#bucketSpec.
    def enterBucketSpec(self, ctx:SparkSqlBaseParser.BucketSpecContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#bucketSpec.
    def exitBucketSpec(self, ctx:SparkSqlBaseParser.BucketSpecContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#skewSpec.
    def enterSkewSpec(self, ctx:SparkSqlBaseParser.SkewSpecContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#skewSpec.
    def exitSkewSpec(self, ctx:SparkSqlBaseParser.SkewSpecContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#locationSpec.
    def enterLocationSpec(self, ctx:SparkSqlBaseParser.LocationSpecContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#locationSpec.
    def exitLocationSpec(self, ctx:SparkSqlBaseParser.LocationSpecContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#query.
    def enterQuery(self, ctx:SparkSqlBaseParser.QueryContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#query.
    def exitQuery(self, ctx:SparkSqlBaseParser.QueryContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#insertOverwriteTable.
    def enterInsertOverwriteTable(self, ctx:SparkSqlBaseParser.InsertOverwriteTableContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#insertOverwriteTable.
    def exitInsertOverwriteTable(self, ctx:SparkSqlBaseParser.InsertOverwriteTableContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#insertIntoTable.
    def enterInsertIntoTable(self, ctx:SparkSqlBaseParser.InsertIntoTableContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#insertIntoTable.
    def exitInsertIntoTable(self, ctx:SparkSqlBaseParser.InsertIntoTableContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#insertOverwriteHiveDir.
    def enterInsertOverwriteHiveDir(self, ctx:SparkSqlBaseParser.InsertOverwriteHiveDirContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#insertOverwriteHiveDir.
    def exitInsertOverwriteHiveDir(self, ctx:SparkSqlBaseParser.InsertOverwriteHiveDirContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#insertOverwriteDir.
    def enterInsertOverwriteDir(self, ctx:SparkSqlBaseParser.InsertOverwriteDirContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#insertOverwriteDir.
    def exitInsertOverwriteDir(self, ctx:SparkSqlBaseParser.InsertOverwriteDirContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#partitionSpecLocation.
    def enterPartitionSpecLocation(self, ctx:SparkSqlBaseParser.PartitionSpecLocationContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#partitionSpecLocation.
    def exitPartitionSpecLocation(self, ctx:SparkSqlBaseParser.PartitionSpecLocationContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#partitionSpec.
    def enterPartitionSpec(self, ctx:SparkSqlBaseParser.PartitionSpecContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#partitionSpec.
    def exitPartitionSpec(self, ctx:SparkSqlBaseParser.PartitionSpecContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#partitionVal.
    def enterPartitionVal(self, ctx:SparkSqlBaseParser.PartitionValContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#partitionVal.
    def exitPartitionVal(self, ctx:SparkSqlBaseParser.PartitionValContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#describeFuncName.
    def enterDescribeFuncName(self, ctx:SparkSqlBaseParser.DescribeFuncNameContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#describeFuncName.
    def exitDescribeFuncName(self, ctx:SparkSqlBaseParser.DescribeFuncNameContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#describeColName.
    def enterDescribeColName(self, ctx:SparkSqlBaseParser.DescribeColNameContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#describeColName.
    def exitDescribeColName(self, ctx:SparkSqlBaseParser.DescribeColNameContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#ctes.
    def enterCtes(self, ctx:SparkSqlBaseParser.CtesContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#ctes.
    def exitCtes(self, ctx:SparkSqlBaseParser.CtesContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#namedQuery.
    def enterNamedQuery(self, ctx:SparkSqlBaseParser.NamedQueryContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#namedQuery.
    def exitNamedQuery(self, ctx:SparkSqlBaseParser.NamedQueryContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#tableProvider.
    def enterTableProvider(self, ctx:SparkSqlBaseParser.TableProviderContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#tableProvider.
    def exitTableProvider(self, ctx:SparkSqlBaseParser.TableProviderContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#tablePropertyList.
    def enterTablePropertyList(self, ctx:SparkSqlBaseParser.TablePropertyListContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#tablePropertyList.
    def exitTablePropertyList(self, ctx:SparkSqlBaseParser.TablePropertyListContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#tableProperty.
    def enterTableProperty(self, ctx:SparkSqlBaseParser.TablePropertyContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#tableProperty.
    def exitTableProperty(self, ctx:SparkSqlBaseParser.TablePropertyContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#tablePropertyKey.
    def enterTablePropertyKey(self, ctx:SparkSqlBaseParser.TablePropertyKeyContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#tablePropertyKey.
    def exitTablePropertyKey(self, ctx:SparkSqlBaseParser.TablePropertyKeyContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#tablePropertyValue.
    def enterTablePropertyValue(self, ctx:SparkSqlBaseParser.TablePropertyValueContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#tablePropertyValue.
    def exitTablePropertyValue(self, ctx:SparkSqlBaseParser.TablePropertyValueContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#constantList.
    def enterConstantList(self, ctx:SparkSqlBaseParser.ConstantListContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#constantList.
    def exitConstantList(self, ctx:SparkSqlBaseParser.ConstantListContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#nestedConstantList.
    def enterNestedConstantList(self, ctx:SparkSqlBaseParser.NestedConstantListContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#nestedConstantList.
    def exitNestedConstantList(self, ctx:SparkSqlBaseParser.NestedConstantListContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#createFileFormat.
    def enterCreateFileFormat(self, ctx:SparkSqlBaseParser.CreateFileFormatContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#createFileFormat.
    def exitCreateFileFormat(self, ctx:SparkSqlBaseParser.CreateFileFormatContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#tableFileFormat.
    def enterTableFileFormat(self, ctx:SparkSqlBaseParser.TableFileFormatContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#tableFileFormat.
    def exitTableFileFormat(self, ctx:SparkSqlBaseParser.TableFileFormatContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#genericFileFormat.
    def enterGenericFileFormat(self, ctx:SparkSqlBaseParser.GenericFileFormatContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#genericFileFormat.
    def exitGenericFileFormat(self, ctx:SparkSqlBaseParser.GenericFileFormatContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#storageHandler.
    def enterStorageHandler(self, ctx:SparkSqlBaseParser.StorageHandlerContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#storageHandler.
    def exitStorageHandler(self, ctx:SparkSqlBaseParser.StorageHandlerContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#resource.
    def enterResource(self, ctx:SparkSqlBaseParser.ResourceContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#resource.
    def exitResource(self, ctx:SparkSqlBaseParser.ResourceContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#singleInsertQuery.
    def enterSingleInsertQuery(self, ctx:SparkSqlBaseParser.SingleInsertQueryContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#singleInsertQuery.
    def exitSingleInsertQuery(self, ctx:SparkSqlBaseParser.SingleInsertQueryContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#multiInsertQuery.
    def enterMultiInsertQuery(self, ctx:SparkSqlBaseParser.MultiInsertQueryContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#multiInsertQuery.
    def exitMultiInsertQuery(self, ctx:SparkSqlBaseParser.MultiInsertQueryContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#queryOrganization.
    def enterQueryOrganization(self, ctx:SparkSqlBaseParser.QueryOrganizationContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#queryOrganization.
    def exitQueryOrganization(self, ctx:SparkSqlBaseParser.QueryOrganizationContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#multiInsertQueryBody.
    def enterMultiInsertQueryBody(self, ctx:SparkSqlBaseParser.MultiInsertQueryBodyContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#multiInsertQueryBody.
    def exitMultiInsertQueryBody(self, ctx:SparkSqlBaseParser.MultiInsertQueryBodyContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#queryTermDefault.
    def enterQueryTermDefault(self, ctx:SparkSqlBaseParser.QueryTermDefaultContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#queryTermDefault.
    def exitQueryTermDefault(self, ctx:SparkSqlBaseParser.QueryTermDefaultContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#setOperation.
    def enterSetOperation(self, ctx:SparkSqlBaseParser.SetOperationContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#setOperation.
    def exitSetOperation(self, ctx:SparkSqlBaseParser.SetOperationContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#queryPrimaryDefault.
    def enterQueryPrimaryDefault(self, ctx:SparkSqlBaseParser.QueryPrimaryDefaultContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#queryPrimaryDefault.
    def exitQueryPrimaryDefault(self, ctx:SparkSqlBaseParser.QueryPrimaryDefaultContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#table.
    def enterTable(self, ctx:SparkSqlBaseParser.TableContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#table.
    def exitTable(self, ctx:SparkSqlBaseParser.TableContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#inlineTableDefault1.
    def enterInlineTableDefault1(self, ctx:SparkSqlBaseParser.InlineTableDefault1Context):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#inlineTableDefault1.
    def exitInlineTableDefault1(self, ctx:SparkSqlBaseParser.InlineTableDefault1Context):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#subquery.
    def enterSubquery(self, ctx:SparkSqlBaseParser.SubqueryContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#subquery.
    def exitSubquery(self, ctx:SparkSqlBaseParser.SubqueryContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#sortItem.
    def enterSortItem(self, ctx:SparkSqlBaseParser.SortItemContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#sortItem.
    def exitSortItem(self, ctx:SparkSqlBaseParser.SortItemContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#querySpecification.
    def enterQuerySpecification(self, ctx:SparkSqlBaseParser.QuerySpecificationContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#querySpecification.
    def exitQuerySpecification(self, ctx:SparkSqlBaseParser.QuerySpecificationContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#hint.
    def enterHint(self, ctx:SparkSqlBaseParser.HintContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#hint.
    def exitHint(self, ctx:SparkSqlBaseParser.HintContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#hintStatement.
    def enterHintStatement(self, ctx:SparkSqlBaseParser.HintStatementContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#hintStatement.
    def exitHintStatement(self, ctx:SparkSqlBaseParser.HintStatementContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#fromClause.
    def enterFromClause(self, ctx:SparkSqlBaseParser.FromClauseContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#fromClause.
    def exitFromClause(self, ctx:SparkSqlBaseParser.FromClauseContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#aggregation.
    def enterAggregation(self, ctx:SparkSqlBaseParser.AggregationContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#aggregation.
    def exitAggregation(self, ctx:SparkSqlBaseParser.AggregationContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#groupingSet.
    def enterGroupingSet(self, ctx:SparkSqlBaseParser.GroupingSetContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#groupingSet.
    def exitGroupingSet(self, ctx:SparkSqlBaseParser.GroupingSetContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#pivotClause.
    def enterPivotClause(self, ctx:SparkSqlBaseParser.PivotClauseContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#pivotClause.
    def exitPivotClause(self, ctx:SparkSqlBaseParser.PivotClauseContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#pivotColumn.
    def enterPivotColumn(self, ctx:SparkSqlBaseParser.PivotColumnContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#pivotColumn.
    def exitPivotColumn(self, ctx:SparkSqlBaseParser.PivotColumnContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#pivotValue.
    def enterPivotValue(self, ctx:SparkSqlBaseParser.PivotValueContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#pivotValue.
    def exitPivotValue(self, ctx:SparkSqlBaseParser.PivotValueContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#lateralView.
    def enterLateralView(self, ctx:SparkSqlBaseParser.LateralViewContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#lateralView.
    def exitLateralView(self, ctx:SparkSqlBaseParser.LateralViewContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#setQuantifier.
    def enterSetQuantifier(self, ctx:SparkSqlBaseParser.SetQuantifierContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#setQuantifier.
    def exitSetQuantifier(self, ctx:SparkSqlBaseParser.SetQuantifierContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#relation.
    def enterRelation(self, ctx:SparkSqlBaseParser.RelationContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#relation.
    def exitRelation(self, ctx:SparkSqlBaseParser.RelationContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#joinRelation.
    def enterJoinRelation(self, ctx:SparkSqlBaseParser.JoinRelationContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#joinRelation.
    def exitJoinRelation(self, ctx:SparkSqlBaseParser.JoinRelationContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#joinType.
    def enterJoinType(self, ctx:SparkSqlBaseParser.JoinTypeContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#joinType.
    def exitJoinType(self, ctx:SparkSqlBaseParser.JoinTypeContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#joinCriteria.
    def enterJoinCriteria(self, ctx:SparkSqlBaseParser.JoinCriteriaContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#joinCriteria.
    def exitJoinCriteria(self, ctx:SparkSqlBaseParser.JoinCriteriaContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#sample.
    def enterSample(self, ctx:SparkSqlBaseParser.SampleContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#sample.
    def exitSample(self, ctx:SparkSqlBaseParser.SampleContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#sampleByPercentile.
    def enterSampleByPercentile(self, ctx:SparkSqlBaseParser.SampleByPercentileContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#sampleByPercentile.
    def exitSampleByPercentile(self, ctx:SparkSqlBaseParser.SampleByPercentileContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#sampleByRows.
    def enterSampleByRows(self, ctx:SparkSqlBaseParser.SampleByRowsContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#sampleByRows.
    def exitSampleByRows(self, ctx:SparkSqlBaseParser.SampleByRowsContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#sampleByBucket.
    def enterSampleByBucket(self, ctx:SparkSqlBaseParser.SampleByBucketContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#sampleByBucket.
    def exitSampleByBucket(self, ctx:SparkSqlBaseParser.SampleByBucketContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#sampleByBytes.
    def enterSampleByBytes(self, ctx:SparkSqlBaseParser.SampleByBytesContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#sampleByBytes.
    def exitSampleByBytes(self, ctx:SparkSqlBaseParser.SampleByBytesContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#identifierList.
    def enterIdentifierList(self, ctx:SparkSqlBaseParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#identifierList.
    def exitIdentifierList(self, ctx:SparkSqlBaseParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#identifierSeq.
    def enterIdentifierSeq(self, ctx:SparkSqlBaseParser.IdentifierSeqContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#identifierSeq.
    def exitIdentifierSeq(self, ctx:SparkSqlBaseParser.IdentifierSeqContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#orderedIdentifierList.
    def enterOrderedIdentifierList(self, ctx:SparkSqlBaseParser.OrderedIdentifierListContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#orderedIdentifierList.
    def exitOrderedIdentifierList(self, ctx:SparkSqlBaseParser.OrderedIdentifierListContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#orderedIdentifier.
    def enterOrderedIdentifier(self, ctx:SparkSqlBaseParser.OrderedIdentifierContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#orderedIdentifier.
    def exitOrderedIdentifier(self, ctx:SparkSqlBaseParser.OrderedIdentifierContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#identifierCommentList.
    def enterIdentifierCommentList(self, ctx:SparkSqlBaseParser.IdentifierCommentListContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#identifierCommentList.
    def exitIdentifierCommentList(self, ctx:SparkSqlBaseParser.IdentifierCommentListContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#identifierComment.
    def enterIdentifierComment(self, ctx:SparkSqlBaseParser.IdentifierCommentContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#identifierComment.
    def exitIdentifierComment(self, ctx:SparkSqlBaseParser.IdentifierCommentContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#tableName.
    def enterTableName(self, ctx:SparkSqlBaseParser.TableNameContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#tableName.
    def exitTableName(self, ctx:SparkSqlBaseParser.TableNameContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#aliasedQuery.
    def enterAliasedQuery(self, ctx:SparkSqlBaseParser.AliasedQueryContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#aliasedQuery.
    def exitAliasedQuery(self, ctx:SparkSqlBaseParser.AliasedQueryContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#aliasedRelation.
    def enterAliasedRelation(self, ctx:SparkSqlBaseParser.AliasedRelationContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#aliasedRelation.
    def exitAliasedRelation(self, ctx:SparkSqlBaseParser.AliasedRelationContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#inlineTableDefault2.
    def enterInlineTableDefault2(self, ctx:SparkSqlBaseParser.InlineTableDefault2Context):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#inlineTableDefault2.
    def exitInlineTableDefault2(self, ctx:SparkSqlBaseParser.InlineTableDefault2Context):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#tableValuedFunction.
    def enterTableValuedFunction(self, ctx:SparkSqlBaseParser.TableValuedFunctionContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#tableValuedFunction.
    def exitTableValuedFunction(self, ctx:SparkSqlBaseParser.TableValuedFunctionContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#inlineTable.
    def enterInlineTable(self, ctx:SparkSqlBaseParser.InlineTableContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#inlineTable.
    def exitInlineTable(self, ctx:SparkSqlBaseParser.InlineTableContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#functionTable.
    def enterFunctionTable(self, ctx:SparkSqlBaseParser.FunctionTableContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#functionTable.
    def exitFunctionTable(self, ctx:SparkSqlBaseParser.FunctionTableContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#tableAlias.
    def enterTableAlias(self, ctx:SparkSqlBaseParser.TableAliasContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#tableAlias.
    def exitTableAlias(self, ctx:SparkSqlBaseParser.TableAliasContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#rowFormatSerde.
    def enterRowFormatSerde(self, ctx:SparkSqlBaseParser.RowFormatSerdeContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#rowFormatSerde.
    def exitRowFormatSerde(self, ctx:SparkSqlBaseParser.RowFormatSerdeContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#rowFormatDelimited.
    def enterRowFormatDelimited(self, ctx:SparkSqlBaseParser.RowFormatDelimitedContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#rowFormatDelimited.
    def exitRowFormatDelimited(self, ctx:SparkSqlBaseParser.RowFormatDelimitedContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#tableIdentifier.
    def enterTableIdentifier(self, ctx:SparkSqlBaseParser.TableIdentifierContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#tableIdentifier.
    def exitTableIdentifier(self, ctx:SparkSqlBaseParser.TableIdentifierContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#functionIdentifier.
    def enterFunctionIdentifier(self, ctx:SparkSqlBaseParser.FunctionIdentifierContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#functionIdentifier.
    def exitFunctionIdentifier(self, ctx:SparkSqlBaseParser.FunctionIdentifierContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#namedExpression.
    def enterNamedExpression(self, ctx:SparkSqlBaseParser.NamedExpressionContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#namedExpression.
    def exitNamedExpression(self, ctx:SparkSqlBaseParser.NamedExpressionContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#namedExpressionSeq.
    def enterNamedExpressionSeq(self, ctx:SparkSqlBaseParser.NamedExpressionSeqContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#namedExpressionSeq.
    def exitNamedExpressionSeq(self, ctx:SparkSqlBaseParser.NamedExpressionSeqContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#expression.
    def enterExpression(self, ctx:SparkSqlBaseParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#expression.
    def exitExpression(self, ctx:SparkSqlBaseParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#logicalNot.
    def enterLogicalNot(self, ctx:SparkSqlBaseParser.LogicalNotContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#logicalNot.
    def exitLogicalNot(self, ctx:SparkSqlBaseParser.LogicalNotContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#predicated.
    def enterPredicated(self, ctx:SparkSqlBaseParser.PredicatedContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#predicated.
    def exitPredicated(self, ctx:SparkSqlBaseParser.PredicatedContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#exists.
    def enterExists(self, ctx:SparkSqlBaseParser.ExistsContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#exists.
    def exitExists(self, ctx:SparkSqlBaseParser.ExistsContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#logicalBinary.
    def enterLogicalBinary(self, ctx:SparkSqlBaseParser.LogicalBinaryContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#logicalBinary.
    def exitLogicalBinary(self, ctx:SparkSqlBaseParser.LogicalBinaryContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#predicate.
    def enterPredicate(self, ctx:SparkSqlBaseParser.PredicateContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#predicate.
    def exitPredicate(self, ctx:SparkSqlBaseParser.PredicateContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#valueExpressionDefault.
    def enterValueExpressionDefault(self, ctx:SparkSqlBaseParser.ValueExpressionDefaultContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#valueExpressionDefault.
    def exitValueExpressionDefault(self, ctx:SparkSqlBaseParser.ValueExpressionDefaultContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#comparison.
    def enterComparison(self, ctx:SparkSqlBaseParser.ComparisonContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#comparison.
    def exitComparison(self, ctx:SparkSqlBaseParser.ComparisonContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#arithmeticBinary.
    def enterArithmeticBinary(self, ctx:SparkSqlBaseParser.ArithmeticBinaryContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#arithmeticBinary.
    def exitArithmeticBinary(self, ctx:SparkSqlBaseParser.ArithmeticBinaryContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#arithmeticUnary.
    def enterArithmeticUnary(self, ctx:SparkSqlBaseParser.ArithmeticUnaryContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#arithmeticUnary.
    def exitArithmeticUnary(self, ctx:SparkSqlBaseParser.ArithmeticUnaryContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#struct.
    def enterStruct(self, ctx:SparkSqlBaseParser.StructContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#struct.
    def exitStruct(self, ctx:SparkSqlBaseParser.StructContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#dereference.
    def enterDereference(self, ctx:SparkSqlBaseParser.DereferenceContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#dereference.
    def exitDereference(self, ctx:SparkSqlBaseParser.DereferenceContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#simpleCase.
    def enterSimpleCase(self, ctx:SparkSqlBaseParser.SimpleCaseContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#simpleCase.
    def exitSimpleCase(self, ctx:SparkSqlBaseParser.SimpleCaseContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#columnReference.
    def enterColumnReference(self, ctx:SparkSqlBaseParser.ColumnReferenceContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#columnReference.
    def exitColumnReference(self, ctx:SparkSqlBaseParser.ColumnReferenceContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#rowConstructor.
    def enterRowConstructor(self, ctx:SparkSqlBaseParser.RowConstructorContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#rowConstructor.
    def exitRowConstructor(self, ctx:SparkSqlBaseParser.RowConstructorContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#last.
    def enterLast(self, ctx:SparkSqlBaseParser.LastContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#last.
    def exitLast(self, ctx:SparkSqlBaseParser.LastContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#star.
    def enterStar(self, ctx:SparkSqlBaseParser.StarContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#star.
    def exitStar(self, ctx:SparkSqlBaseParser.StarContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#subscript.
    def enterSubscript(self, ctx:SparkSqlBaseParser.SubscriptContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#subscript.
    def exitSubscript(self, ctx:SparkSqlBaseParser.SubscriptContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#subqueryExpression.
    def enterSubqueryExpression(self, ctx:SparkSqlBaseParser.SubqueryExpressionContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#subqueryExpression.
    def exitSubqueryExpression(self, ctx:SparkSqlBaseParser.SubqueryExpressionContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#cast.
    def enterCast(self, ctx:SparkSqlBaseParser.CastContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#cast.
    def exitCast(self, ctx:SparkSqlBaseParser.CastContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#constantDefault.
    def enterConstantDefault(self, ctx:SparkSqlBaseParser.ConstantDefaultContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#constantDefault.
    def exitConstantDefault(self, ctx:SparkSqlBaseParser.ConstantDefaultContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#lambda.
    def enterLambda(self, ctx:SparkSqlBaseParser.LambdaContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#lambda.
    def exitLambda(self, ctx:SparkSqlBaseParser.LambdaContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#parenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:SparkSqlBaseParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#parenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:SparkSqlBaseParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#extract.
    def enterExtract(self, ctx:SparkSqlBaseParser.ExtractContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#extract.
    def exitExtract(self, ctx:SparkSqlBaseParser.ExtractContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#functionCall.
    def enterFunctionCall(self, ctx:SparkSqlBaseParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#functionCall.
    def exitFunctionCall(self, ctx:SparkSqlBaseParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#searchedCase.
    def enterSearchedCase(self, ctx:SparkSqlBaseParser.SearchedCaseContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#searchedCase.
    def exitSearchedCase(self, ctx:SparkSqlBaseParser.SearchedCaseContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#position.
    def enterPosition(self, ctx:SparkSqlBaseParser.PositionContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#position.
    def exitPosition(self, ctx:SparkSqlBaseParser.PositionContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#first.
    def enterFirst(self, ctx:SparkSqlBaseParser.FirstContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#first.
    def exitFirst(self, ctx:SparkSqlBaseParser.FirstContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#nullLiteral.
    def enterNullLiteral(self, ctx:SparkSqlBaseParser.NullLiteralContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#nullLiteral.
    def exitNullLiteral(self, ctx:SparkSqlBaseParser.NullLiteralContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#intervalLiteral.
    def enterIntervalLiteral(self, ctx:SparkSqlBaseParser.IntervalLiteralContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#intervalLiteral.
    def exitIntervalLiteral(self, ctx:SparkSqlBaseParser.IntervalLiteralContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#typeConstructor.
    def enterTypeConstructor(self, ctx:SparkSqlBaseParser.TypeConstructorContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#typeConstructor.
    def exitTypeConstructor(self, ctx:SparkSqlBaseParser.TypeConstructorContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#numericLiteral.
    def enterNumericLiteral(self, ctx:SparkSqlBaseParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#numericLiteral.
    def exitNumericLiteral(self, ctx:SparkSqlBaseParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:SparkSqlBaseParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:SparkSqlBaseParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#stringLiteral.
    def enterStringLiteral(self, ctx:SparkSqlBaseParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#stringLiteral.
    def exitStringLiteral(self, ctx:SparkSqlBaseParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:SparkSqlBaseParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:SparkSqlBaseParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#arithmeticOperator.
    def enterArithmeticOperator(self, ctx:SparkSqlBaseParser.ArithmeticOperatorContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#arithmeticOperator.
    def exitArithmeticOperator(self, ctx:SparkSqlBaseParser.ArithmeticOperatorContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#predicateOperator.
    def enterPredicateOperator(self, ctx:SparkSqlBaseParser.PredicateOperatorContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#predicateOperator.
    def exitPredicateOperator(self, ctx:SparkSqlBaseParser.PredicateOperatorContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#booleanValue.
    def enterBooleanValue(self, ctx:SparkSqlBaseParser.BooleanValueContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#booleanValue.
    def exitBooleanValue(self, ctx:SparkSqlBaseParser.BooleanValueContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#interval.
    def enterInterval(self, ctx:SparkSqlBaseParser.IntervalContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#interval.
    def exitInterval(self, ctx:SparkSqlBaseParser.IntervalContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#intervalField.
    def enterIntervalField(self, ctx:SparkSqlBaseParser.IntervalFieldContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#intervalField.
    def exitIntervalField(self, ctx:SparkSqlBaseParser.IntervalFieldContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#intervalValue.
    def enterIntervalValue(self, ctx:SparkSqlBaseParser.IntervalValueContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#intervalValue.
    def exitIntervalValue(self, ctx:SparkSqlBaseParser.IntervalValueContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#colPosition.
    def enterColPosition(self, ctx:SparkSqlBaseParser.ColPositionContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#colPosition.
    def exitColPosition(self, ctx:SparkSqlBaseParser.ColPositionContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#complex_DataType.
    def enterComplex_DataType(self, ctx:SparkSqlBaseParser.Complex_DataTypeContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#complex_DataType.
    def exitComplex_DataType(self, ctx:SparkSqlBaseParser.Complex_DataTypeContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#primitiveDataType.
    def enterPrimitiveDataType(self, ctx:SparkSqlBaseParser.PrimitiveDataTypeContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#primitiveDataType.
    def exitPrimitiveDataType(self, ctx:SparkSqlBaseParser.PrimitiveDataTypeContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#colTypeList.
    def enterColTypeList(self, ctx:SparkSqlBaseParser.ColTypeListContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#colTypeList.
    def exitColTypeList(self, ctx:SparkSqlBaseParser.ColTypeListContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#colType.
    def enterColType(self, ctx:SparkSqlBaseParser.ColTypeContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#colType.
    def exitColType(self, ctx:SparkSqlBaseParser.ColTypeContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#complex_ColTypeList.
    def enterComplex_ColTypeList(self, ctx:SparkSqlBaseParser.Complex_ColTypeListContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#complex_ColTypeList.
    def exitComplex_ColTypeList(self, ctx:SparkSqlBaseParser.Complex_ColTypeListContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#complex_ColType.
    def enterComplex_ColType(self, ctx:SparkSqlBaseParser.Complex_ColTypeContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#complex_ColType.
    def exitComplex_ColType(self, ctx:SparkSqlBaseParser.Complex_ColTypeContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#whenClause.
    def enterWhenClause(self, ctx:SparkSqlBaseParser.WhenClauseContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#whenClause.
    def exitWhenClause(self, ctx:SparkSqlBaseParser.WhenClauseContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#windows.
    def enterWindows(self, ctx:SparkSqlBaseParser.WindowsContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#windows.
    def exitWindows(self, ctx:SparkSqlBaseParser.WindowsContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#namedWindow.
    def enterNamedWindow(self, ctx:SparkSqlBaseParser.NamedWindowContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#namedWindow.
    def exitNamedWindow(self, ctx:SparkSqlBaseParser.NamedWindowContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#windowRef.
    def enterWindowRef(self, ctx:SparkSqlBaseParser.WindowRefContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#windowRef.
    def exitWindowRef(self, ctx:SparkSqlBaseParser.WindowRefContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#windowDef.
    def enterWindowDef(self, ctx:SparkSqlBaseParser.WindowDefContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#windowDef.
    def exitWindowDef(self, ctx:SparkSqlBaseParser.WindowDefContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#windowFrame.
    def enterWindowFrame(self, ctx:SparkSqlBaseParser.WindowFrameContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#windowFrame.
    def exitWindowFrame(self, ctx:SparkSqlBaseParser.WindowFrameContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#frameBound.
    def enterFrameBound(self, ctx:SparkSqlBaseParser.FrameBoundContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#frameBound.
    def exitFrameBound(self, ctx:SparkSqlBaseParser.FrameBoundContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#qualifiedName.
    def enterQualifiedName(self, ctx:SparkSqlBaseParser.QualifiedNameContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#qualifiedName.
    def exitQualifiedName(self, ctx:SparkSqlBaseParser.QualifiedNameContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#identifier.
    def enterIdentifier(self, ctx:SparkSqlBaseParser.IdentifierContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#identifier.
    def exitIdentifier(self, ctx:SparkSqlBaseParser.IdentifierContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#unquotedIdentifier.
    def enterUnquotedIdentifier(self, ctx:SparkSqlBaseParser.UnquotedIdentifierContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#unquotedIdentifier.
    def exitUnquotedIdentifier(self, ctx:SparkSqlBaseParser.UnquotedIdentifierContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#quotedIdentifierAlternative.
    def enterQuotedIdentifierAlternative(self, ctx:SparkSqlBaseParser.QuotedIdentifierAlternativeContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#quotedIdentifierAlternative.
    def exitQuotedIdentifierAlternative(self, ctx:SparkSqlBaseParser.QuotedIdentifierAlternativeContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#quotedIdentifier.
    def enterQuotedIdentifier(self, ctx:SparkSqlBaseParser.QuotedIdentifierContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#quotedIdentifier.
    def exitQuotedIdentifier(self, ctx:SparkSqlBaseParser.QuotedIdentifierContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#decimalLiteral.
    def enterDecimalLiteral(self, ctx:SparkSqlBaseParser.DecimalLiteralContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#decimalLiteral.
    def exitDecimalLiteral(self, ctx:SparkSqlBaseParser.DecimalLiteralContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#integerLiteral.
    def enterIntegerLiteral(self, ctx:SparkSqlBaseParser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#integerLiteral.
    def exitIntegerLiteral(self, ctx:SparkSqlBaseParser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#bigIntLiteral.
    def enterBigIntLiteral(self, ctx:SparkSqlBaseParser.BigIntLiteralContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#bigIntLiteral.
    def exitBigIntLiteral(self, ctx:SparkSqlBaseParser.BigIntLiteralContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#smallIntLiteral.
    def enterSmallIntLiteral(self, ctx:SparkSqlBaseParser.SmallIntLiteralContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#smallIntLiteral.
    def exitSmallIntLiteral(self, ctx:SparkSqlBaseParser.SmallIntLiteralContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#tinyIntLiteral.
    def enterTinyIntLiteral(self, ctx:SparkSqlBaseParser.TinyIntLiteralContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#tinyIntLiteral.
    def exitTinyIntLiteral(self, ctx:SparkSqlBaseParser.TinyIntLiteralContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#doubleLiteral.
    def enterDoubleLiteral(self, ctx:SparkSqlBaseParser.DoubleLiteralContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#doubleLiteral.
    def exitDoubleLiteral(self, ctx:SparkSqlBaseParser.DoubleLiteralContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#bigDecimalLiteral.
    def enterBigDecimalLiteral(self, ctx:SparkSqlBaseParser.BigDecimalLiteralContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#bigDecimalLiteral.
    def exitBigDecimalLiteral(self, ctx:SparkSqlBaseParser.BigDecimalLiteralContext):
        pass


    # Enter a parse tree produced by SparkSqlBaseParser#nonReserved.
    def enterNonReserved(self, ctx:SparkSqlBaseParser.NonReservedContext):
        pass

    # Exit a parse tree produced by SparkSqlBaseParser#nonReserved.
    def exitNonReserved(self, ctx:SparkSqlBaseParser.NonReservedContext):
        pass


