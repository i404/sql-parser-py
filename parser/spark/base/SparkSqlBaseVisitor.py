# Generated from SparkSqlBase.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SparkSqlBaseParser import SparkSqlBaseParser
else:
    from SparkSqlBaseParser import SparkSqlBaseParser

# This class defines a complete generic visitor for a parse tree produced by SparkSqlBaseParser.

class SparkSqlBaseVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SparkSqlBaseParser#singleStatement.
    def visitSingleStatement(self, ctx:SparkSqlBaseParser.SingleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#singleExpression.
    def visitSingleExpression(self, ctx:SparkSqlBaseParser.SingleExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#singleTableIdentifier.
    def visitSingleTableIdentifier(self, ctx:SparkSqlBaseParser.SingleTableIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#singleFunctionIdentifier.
    def visitSingleFunctionIdentifier(self, ctx:SparkSqlBaseParser.SingleFunctionIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#singleDataType.
    def visitSingleDataType(self, ctx:SparkSqlBaseParser.SingleDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#singleTableSchema.
    def visitSingleTableSchema(self, ctx:SparkSqlBaseParser.SingleTableSchemaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#statementDefault.
    def visitStatementDefault(self, ctx:SparkSqlBaseParser.StatementDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#use.
    def visitUse(self, ctx:SparkSqlBaseParser.UseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#createDatabase.
    def visitCreateDatabase(self, ctx:SparkSqlBaseParser.CreateDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#setDatabaseProperties.
    def visitSetDatabaseProperties(self, ctx:SparkSqlBaseParser.SetDatabasePropertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#dropDatabase.
    def visitDropDatabase(self, ctx:SparkSqlBaseParser.DropDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#createTable.
    def visitCreateTable(self, ctx:SparkSqlBaseParser.CreateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#createHiveTable.
    def visitCreateHiveTable(self, ctx:SparkSqlBaseParser.CreateHiveTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#createTableLike.
    def visitCreateTableLike(self, ctx:SparkSqlBaseParser.CreateTableLikeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#analyze.
    def visitAnalyze(self, ctx:SparkSqlBaseParser.AnalyzeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#addTableColumns.
    def visitAddTableColumns(self, ctx:SparkSqlBaseParser.AddTableColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#renameTable.
    def visitRenameTable(self, ctx:SparkSqlBaseParser.RenameTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#setTableProperties.
    def visitSetTableProperties(self, ctx:SparkSqlBaseParser.SetTablePropertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#unsetTableProperties.
    def visitUnsetTableProperties(self, ctx:SparkSqlBaseParser.UnsetTablePropertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#changeColumn.
    def visitChangeColumn(self, ctx:SparkSqlBaseParser.ChangeColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#setTableSerDe.
    def visitSetTableSerDe(self, ctx:SparkSqlBaseParser.SetTableSerDeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#addTablePartition.
    def visitAddTablePartition(self, ctx:SparkSqlBaseParser.AddTablePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#renameTablePartition.
    def visitRenameTablePartition(self, ctx:SparkSqlBaseParser.RenameTablePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#dropTablePartitions.
    def visitDropTablePartitions(self, ctx:SparkSqlBaseParser.DropTablePartitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#setTableLocation.
    def visitSetTableLocation(self, ctx:SparkSqlBaseParser.SetTableLocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#recoverPartitions.
    def visitRecoverPartitions(self, ctx:SparkSqlBaseParser.RecoverPartitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#dropTable.
    def visitDropTable(self, ctx:SparkSqlBaseParser.DropTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#createView.
    def visitCreateView(self, ctx:SparkSqlBaseParser.CreateViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#createTempViewUsing.
    def visitCreateTempViewUsing(self, ctx:SparkSqlBaseParser.CreateTempViewUsingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#alterViewQuery.
    def visitAlterViewQuery(self, ctx:SparkSqlBaseParser.AlterViewQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#createFunction.
    def visitCreateFunction(self, ctx:SparkSqlBaseParser.CreateFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#dropFunction.
    def visitDropFunction(self, ctx:SparkSqlBaseParser.DropFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#explain.
    def visitExplain(self, ctx:SparkSqlBaseParser.ExplainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#showTables.
    def visitShowTables(self, ctx:SparkSqlBaseParser.ShowTablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#showTable.
    def visitShowTable(self, ctx:SparkSqlBaseParser.ShowTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#showDatabases.
    def visitShowDatabases(self, ctx:SparkSqlBaseParser.ShowDatabasesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#showTblProperties.
    def visitShowTblProperties(self, ctx:SparkSqlBaseParser.ShowTblPropertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#showColumns.
    def visitShowColumns(self, ctx:SparkSqlBaseParser.ShowColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#showPartitions.
    def visitShowPartitions(self, ctx:SparkSqlBaseParser.ShowPartitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#showFunctions.
    def visitShowFunctions(self, ctx:SparkSqlBaseParser.ShowFunctionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#showCreateTable.
    def visitShowCreateTable(self, ctx:SparkSqlBaseParser.ShowCreateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#describeFunction.
    def visitDescribeFunction(self, ctx:SparkSqlBaseParser.DescribeFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#describeDatabase.
    def visitDescribeDatabase(self, ctx:SparkSqlBaseParser.DescribeDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#describeTable.
    def visitDescribeTable(self, ctx:SparkSqlBaseParser.DescribeTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#refreshTable.
    def visitRefreshTable(self, ctx:SparkSqlBaseParser.RefreshTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#refreshResource.
    def visitRefreshResource(self, ctx:SparkSqlBaseParser.RefreshResourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#cacheTable.
    def visitCacheTable(self, ctx:SparkSqlBaseParser.CacheTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#uncacheTable.
    def visitUncacheTable(self, ctx:SparkSqlBaseParser.UncacheTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#clearCache.
    def visitClearCache(self, ctx:SparkSqlBaseParser.ClearCacheContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#loadData.
    def visitLoadData(self, ctx:SparkSqlBaseParser.LoadDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#truncateTable.
    def visitTruncateTable(self, ctx:SparkSqlBaseParser.TruncateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#repairTable.
    def visitRepairTable(self, ctx:SparkSqlBaseParser.RepairTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#manageResource.
    def visitManageResource(self, ctx:SparkSqlBaseParser.ManageResourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#failNativeCommand.
    def visitFailNativeCommand(self, ctx:SparkSqlBaseParser.FailNativeCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#setConfiguration.
    def visitSetConfiguration(self, ctx:SparkSqlBaseParser.SetConfigurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#resetConfiguration.
    def visitResetConfiguration(self, ctx:SparkSqlBaseParser.ResetConfigurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#unsupportedHiveNativeCommands.
    def visitUnsupportedHiveNativeCommands(self, ctx:SparkSqlBaseParser.UnsupportedHiveNativeCommandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#createTableHeader.
    def visitCreateTableHeader(self, ctx:SparkSqlBaseParser.CreateTableHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#bucketSpec.
    def visitBucketSpec(self, ctx:SparkSqlBaseParser.BucketSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#skewSpec.
    def visitSkewSpec(self, ctx:SparkSqlBaseParser.SkewSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#locationSpec.
    def visitLocationSpec(self, ctx:SparkSqlBaseParser.LocationSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#query.
    def visitQuery(self, ctx:SparkSqlBaseParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#insertOverwriteTable.
    def visitInsertOverwriteTable(self, ctx:SparkSqlBaseParser.InsertOverwriteTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#insertIntoTable.
    def visitInsertIntoTable(self, ctx:SparkSqlBaseParser.InsertIntoTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#insertOverwriteHiveDir.
    def visitInsertOverwriteHiveDir(self, ctx:SparkSqlBaseParser.InsertOverwriteHiveDirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#insertOverwriteDir.
    def visitInsertOverwriteDir(self, ctx:SparkSqlBaseParser.InsertOverwriteDirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#partitionSpecLocation.
    def visitPartitionSpecLocation(self, ctx:SparkSqlBaseParser.PartitionSpecLocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#partitionSpec.
    def visitPartitionSpec(self, ctx:SparkSqlBaseParser.PartitionSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#partitionVal.
    def visitPartitionVal(self, ctx:SparkSqlBaseParser.PartitionValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#describeFuncName.
    def visitDescribeFuncName(self, ctx:SparkSqlBaseParser.DescribeFuncNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#describeColName.
    def visitDescribeColName(self, ctx:SparkSqlBaseParser.DescribeColNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#ctes.
    def visitCtes(self, ctx:SparkSqlBaseParser.CtesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#namedQuery.
    def visitNamedQuery(self, ctx:SparkSqlBaseParser.NamedQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#tableProvider.
    def visitTableProvider(self, ctx:SparkSqlBaseParser.TableProviderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#tablePropertyList.
    def visitTablePropertyList(self, ctx:SparkSqlBaseParser.TablePropertyListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#tableProperty.
    def visitTableProperty(self, ctx:SparkSqlBaseParser.TablePropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#tablePropertyKey.
    def visitTablePropertyKey(self, ctx:SparkSqlBaseParser.TablePropertyKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#tablePropertyValue.
    def visitTablePropertyValue(self, ctx:SparkSqlBaseParser.TablePropertyValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#constantList.
    def visitConstantList(self, ctx:SparkSqlBaseParser.ConstantListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#nestedConstantList.
    def visitNestedConstantList(self, ctx:SparkSqlBaseParser.NestedConstantListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#createFileFormat.
    def visitCreateFileFormat(self, ctx:SparkSqlBaseParser.CreateFileFormatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#tableFileFormat.
    def visitTableFileFormat(self, ctx:SparkSqlBaseParser.TableFileFormatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#genericFileFormat.
    def visitGenericFileFormat(self, ctx:SparkSqlBaseParser.GenericFileFormatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#storageHandler.
    def visitStorageHandler(self, ctx:SparkSqlBaseParser.StorageHandlerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#resource.
    def visitResource(self, ctx:SparkSqlBaseParser.ResourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#singleInsertQuery.
    def visitSingleInsertQuery(self, ctx:SparkSqlBaseParser.SingleInsertQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#multiInsertQuery.
    def visitMultiInsertQuery(self, ctx:SparkSqlBaseParser.MultiInsertQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#queryOrganization.
    def visitQueryOrganization(self, ctx:SparkSqlBaseParser.QueryOrganizationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#multiInsertQueryBody.
    def visitMultiInsertQueryBody(self, ctx:SparkSqlBaseParser.MultiInsertQueryBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#queryTermDefault.
    def visitQueryTermDefault(self, ctx:SparkSqlBaseParser.QueryTermDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#setOperation.
    def visitSetOperation(self, ctx:SparkSqlBaseParser.SetOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#queryPrimaryDefault.
    def visitQueryPrimaryDefault(self, ctx:SparkSqlBaseParser.QueryPrimaryDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#table.
    def visitTable(self, ctx:SparkSqlBaseParser.TableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#inlineTableDefault1.
    def visitInlineTableDefault1(self, ctx:SparkSqlBaseParser.InlineTableDefault1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#subquery.
    def visitSubquery(self, ctx:SparkSqlBaseParser.SubqueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#sortItem.
    def visitSortItem(self, ctx:SparkSqlBaseParser.SortItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#querySpecification.
    def visitQuerySpecification(self, ctx:SparkSqlBaseParser.QuerySpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#hint.
    def visitHint(self, ctx:SparkSqlBaseParser.HintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#hintStatement.
    def visitHintStatement(self, ctx:SparkSqlBaseParser.HintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#fromClause.
    def visitFromClause(self, ctx:SparkSqlBaseParser.FromClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#aggregation.
    def visitAggregation(self, ctx:SparkSqlBaseParser.AggregationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#groupingSet.
    def visitGroupingSet(self, ctx:SparkSqlBaseParser.GroupingSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#pivotClause.
    def visitPivotClause(self, ctx:SparkSqlBaseParser.PivotClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#pivotColumn.
    def visitPivotColumn(self, ctx:SparkSqlBaseParser.PivotColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#pivotValue.
    def visitPivotValue(self, ctx:SparkSqlBaseParser.PivotValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#lateralView.
    def visitLateralView(self, ctx:SparkSqlBaseParser.LateralViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#setQuantifier.
    def visitSetQuantifier(self, ctx:SparkSqlBaseParser.SetQuantifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#relation.
    def visitRelation(self, ctx:SparkSqlBaseParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#joinRelation.
    def visitJoinRelation(self, ctx:SparkSqlBaseParser.JoinRelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#joinType.
    def visitJoinType(self, ctx:SparkSqlBaseParser.JoinTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#joinCriteria.
    def visitJoinCriteria(self, ctx:SparkSqlBaseParser.JoinCriteriaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#sample.
    def visitSample(self, ctx:SparkSqlBaseParser.SampleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#sampleByPercentile.
    def visitSampleByPercentile(self, ctx:SparkSqlBaseParser.SampleByPercentileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#sampleByRows.
    def visitSampleByRows(self, ctx:SparkSqlBaseParser.SampleByRowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#sampleByBucket.
    def visitSampleByBucket(self, ctx:SparkSqlBaseParser.SampleByBucketContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#sampleByBytes.
    def visitSampleByBytes(self, ctx:SparkSqlBaseParser.SampleByBytesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#identifierList.
    def visitIdentifierList(self, ctx:SparkSqlBaseParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#identifierSeq.
    def visitIdentifierSeq(self, ctx:SparkSqlBaseParser.IdentifierSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#orderedIdentifierList.
    def visitOrderedIdentifierList(self, ctx:SparkSqlBaseParser.OrderedIdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#orderedIdentifier.
    def visitOrderedIdentifier(self, ctx:SparkSqlBaseParser.OrderedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#identifierCommentList.
    def visitIdentifierCommentList(self, ctx:SparkSqlBaseParser.IdentifierCommentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#identifierComment.
    def visitIdentifierComment(self, ctx:SparkSqlBaseParser.IdentifierCommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#tableName.
    def visitTableName(self, ctx:SparkSqlBaseParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#aliasedQuery.
    def visitAliasedQuery(self, ctx:SparkSqlBaseParser.AliasedQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#aliasedRelation.
    def visitAliasedRelation(self, ctx:SparkSqlBaseParser.AliasedRelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#inlineTableDefault2.
    def visitInlineTableDefault2(self, ctx:SparkSqlBaseParser.InlineTableDefault2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#tableValuedFunction.
    def visitTableValuedFunction(self, ctx:SparkSqlBaseParser.TableValuedFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#inlineTable.
    def visitInlineTable(self, ctx:SparkSqlBaseParser.InlineTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#functionTable.
    def visitFunctionTable(self, ctx:SparkSqlBaseParser.FunctionTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#tableAlias.
    def visitTableAlias(self, ctx:SparkSqlBaseParser.TableAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#rowFormatSerde.
    def visitRowFormatSerde(self, ctx:SparkSqlBaseParser.RowFormatSerdeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#rowFormatDelimited.
    def visitRowFormatDelimited(self, ctx:SparkSqlBaseParser.RowFormatDelimitedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#tableIdentifier.
    def visitTableIdentifier(self, ctx:SparkSqlBaseParser.TableIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#functionIdentifier.
    def visitFunctionIdentifier(self, ctx:SparkSqlBaseParser.FunctionIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#namedExpression.
    def visitNamedExpression(self, ctx:SparkSqlBaseParser.NamedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#namedExpressionSeq.
    def visitNamedExpressionSeq(self, ctx:SparkSqlBaseParser.NamedExpressionSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#expression.
    def visitExpression(self, ctx:SparkSqlBaseParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#logicalNot.
    def visitLogicalNot(self, ctx:SparkSqlBaseParser.LogicalNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#predicated.
    def visitPredicated(self, ctx:SparkSqlBaseParser.PredicatedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#exists.
    def visitExists(self, ctx:SparkSqlBaseParser.ExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#logicalBinary.
    def visitLogicalBinary(self, ctx:SparkSqlBaseParser.LogicalBinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#predicate.
    def visitPredicate(self, ctx:SparkSqlBaseParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#valueExpressionDefault.
    def visitValueExpressionDefault(self, ctx:SparkSqlBaseParser.ValueExpressionDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#comparison.
    def visitComparison(self, ctx:SparkSqlBaseParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#arithmeticBinary.
    def visitArithmeticBinary(self, ctx:SparkSqlBaseParser.ArithmeticBinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#arithmeticUnary.
    def visitArithmeticUnary(self, ctx:SparkSqlBaseParser.ArithmeticUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#struct.
    def visitStruct(self, ctx:SparkSqlBaseParser.StructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#dereference.
    def visitDereference(self, ctx:SparkSqlBaseParser.DereferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#simpleCase.
    def visitSimpleCase(self, ctx:SparkSqlBaseParser.SimpleCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#columnReference.
    def visitColumnReference(self, ctx:SparkSqlBaseParser.ColumnReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#rowConstructor.
    def visitRowConstructor(self, ctx:SparkSqlBaseParser.RowConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#last.
    def visitLast(self, ctx:SparkSqlBaseParser.LastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#star.
    def visitStar(self, ctx:SparkSqlBaseParser.StarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#subscript.
    def visitSubscript(self, ctx:SparkSqlBaseParser.SubscriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#subqueryExpression.
    def visitSubqueryExpression(self, ctx:SparkSqlBaseParser.SubqueryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#cast.
    def visitCast(self, ctx:SparkSqlBaseParser.CastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#constantDefault.
    def visitConstantDefault(self, ctx:SparkSqlBaseParser.ConstantDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#lambda.
    def visitLambda(self, ctx:SparkSqlBaseParser.LambdaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#parenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:SparkSqlBaseParser.ParenthesizedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#extract.
    def visitExtract(self, ctx:SparkSqlBaseParser.ExtractContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#functionCall.
    def visitFunctionCall(self, ctx:SparkSqlBaseParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#searchedCase.
    def visitSearchedCase(self, ctx:SparkSqlBaseParser.SearchedCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#position.
    def visitPosition(self, ctx:SparkSqlBaseParser.PositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#first.
    def visitFirst(self, ctx:SparkSqlBaseParser.FirstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#nullLiteral.
    def visitNullLiteral(self, ctx:SparkSqlBaseParser.NullLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#intervalLiteral.
    def visitIntervalLiteral(self, ctx:SparkSqlBaseParser.IntervalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#typeConstructor.
    def visitTypeConstructor(self, ctx:SparkSqlBaseParser.TypeConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#numericLiteral.
    def visitNumericLiteral(self, ctx:SparkSqlBaseParser.NumericLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:SparkSqlBaseParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#stringLiteral.
    def visitStringLiteral(self, ctx:SparkSqlBaseParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:SparkSqlBaseParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#arithmeticOperator.
    def visitArithmeticOperator(self, ctx:SparkSqlBaseParser.ArithmeticOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#predicateOperator.
    def visitPredicateOperator(self, ctx:SparkSqlBaseParser.PredicateOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#booleanValue.
    def visitBooleanValue(self, ctx:SparkSqlBaseParser.BooleanValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#interval.
    def visitInterval(self, ctx:SparkSqlBaseParser.IntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#intervalField.
    def visitIntervalField(self, ctx:SparkSqlBaseParser.IntervalFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#intervalValue.
    def visitIntervalValue(self, ctx:SparkSqlBaseParser.IntervalValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#colPosition.
    def visitColPosition(self, ctx:SparkSqlBaseParser.ColPositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#complex_DataType.
    def visitComplex_DataType(self, ctx:SparkSqlBaseParser.Complex_DataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#primitiveDataType.
    def visitPrimitiveDataType(self, ctx:SparkSqlBaseParser.PrimitiveDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#colTypeList.
    def visitColTypeList(self, ctx:SparkSqlBaseParser.ColTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#colType.
    def visitColType(self, ctx:SparkSqlBaseParser.ColTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#complex_ColTypeList.
    def visitComplex_ColTypeList(self, ctx:SparkSqlBaseParser.Complex_ColTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#complex_ColType.
    def visitComplex_ColType(self, ctx:SparkSqlBaseParser.Complex_ColTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#whenClause.
    def visitWhenClause(self, ctx:SparkSqlBaseParser.WhenClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#windows.
    def visitWindows(self, ctx:SparkSqlBaseParser.WindowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#namedWindow.
    def visitNamedWindow(self, ctx:SparkSqlBaseParser.NamedWindowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#windowRef.
    def visitWindowRef(self, ctx:SparkSqlBaseParser.WindowRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#windowDef.
    def visitWindowDef(self, ctx:SparkSqlBaseParser.WindowDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#windowFrame.
    def visitWindowFrame(self, ctx:SparkSqlBaseParser.WindowFrameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#frameBound.
    def visitFrameBound(self, ctx:SparkSqlBaseParser.FrameBoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#qualifiedName.
    def visitQualifiedName(self, ctx:SparkSqlBaseParser.QualifiedNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#identifier.
    def visitIdentifier(self, ctx:SparkSqlBaseParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#unquotedIdentifier.
    def visitUnquotedIdentifier(self, ctx:SparkSqlBaseParser.UnquotedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#quotedIdentifierAlternative.
    def visitQuotedIdentifierAlternative(self, ctx:SparkSqlBaseParser.QuotedIdentifierAlternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#quotedIdentifier.
    def visitQuotedIdentifier(self, ctx:SparkSqlBaseParser.QuotedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#decimalLiteral.
    def visitDecimalLiteral(self, ctx:SparkSqlBaseParser.DecimalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#integerLiteral.
    def visitIntegerLiteral(self, ctx:SparkSqlBaseParser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#bigIntLiteral.
    def visitBigIntLiteral(self, ctx:SparkSqlBaseParser.BigIntLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#smallIntLiteral.
    def visitSmallIntLiteral(self, ctx:SparkSqlBaseParser.SmallIntLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#tinyIntLiteral.
    def visitTinyIntLiteral(self, ctx:SparkSqlBaseParser.TinyIntLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#doubleLiteral.
    def visitDoubleLiteral(self, ctx:SparkSqlBaseParser.DoubleLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#bigDecimalLiteral.
    def visitBigDecimalLiteral(self, ctx:SparkSqlBaseParser.BigDecimalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSqlBaseParser#nonReserved.
    def visitNonReserved(self, ctx:SparkSqlBaseParser.NonReservedContext):
        return self.visitChildren(ctx)



del SparkSqlBaseParser