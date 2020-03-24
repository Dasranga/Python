# Create empty dictionary

colLength = [
    '8', '8', '8', '3', '15', '10', '10', '10', '10', '200', '10', '10', '20', '10', '10', '4', '10', '20', '38', '20',
    '10', '10', '1', '10', '200', '26', '200', '100', '200', '100', '10', '10', '40', '10', '10', '10', '20', '10',
    '60', '5', '19', '19', '19', '1', '100', '20', '20', '10', '10', '3', '20', '10', '10', '20', '10', '10', '10',
    '10', '40', '10', '10', '5', '100', '100', '10', '5', '3', '1', '8', '8', '8', '8', '10', '8', '30', '200', '10',
    '10', '19', '10', '10', '200', '600', '1', '1', '1', '1', '8', '8', '200', '10', '200', '100']

colNames = ['AcctNo', 'CardLogo', 'PlasticType', 'CycNo', 'CorpCd', 'Sts', 'OverrideSts', 'OverrideStsStart',
            'OverrideStsExpiry', 'OverrideStsUserId', 'EntityId', 'PayeeCd', 'SAPNo', 'ClientClass', 'ClientType',
            'PrcsId', 'ApplId', 'ApplRef', 'SrcRefNo', 'SrcCd', 'InputSrc', 'CautionCd', 'PriceShieldInd', 'CmpyType',
            'CmpyLegalName', 'CmpyEmbName', 'CmpyRegsName1', 'CmpyRegsName2', 'CmpyName1', 'CmpyName2', 'RiskCategory',
            'AssessmentType', 'TaxId', 'BusnCategory', 'ClientClass1', 'ClientType1', 'CmpyRegsNo', 'RegsDate',
            'RegsLocation', 'Shareholder', 'Capital', 'NetSales', 'NetProfit', 'RequiredReport', 'RcptName', 'RcptTel',
            'RcptFax', 'PymtMode', 'PymtTerms', 'GracePeriod', 'PymtAmt', 'BankCd', 'BankAcctType', 'BankAcctNo',
            'BankBranchCd', 'AcctType', 'BillingType', 'DeliveryType', 'SendingCd', 'BranchCd', 'SaleTerritory',
            'SaleLevel', 'ApplIntroBy', 'Remarks', 'WebPw', 'CardSeq', 'AgeingInd', 'AutoReinstate', 'CaptDate',
            'WriteOffDate', 'TerminatedDate', 'BlockDate', 'ReasonCd', 'ExpiryDate', 'TradeNo', 'CustSvcId',
            'GovernmentLevyFeeCd', 'ReloadTxnCnt', 'LoyaltyCardNo', 'BusnEstablishment', 'SIC', 'WebUserId', 'Nob',
            'RcptPrintInd', 'InvBillInd', 'PymtInd', 'VehPerfRptInd', 'MigrateId', 'LastUpdDate', 'UserId',
            'CreationDate', 'CreatedBy', 'SAPName']

dictionary = dict(zip(colNames, colLength))
print(dictionary)

# def getSubStringQuery(subStringQuery, i, crTable):
# getSubStringQuery(subStringQuery, i, crTable)

newTableName = "new_table"
sourceTableName = "source_table"
crTable = "CREATE TABLE " + newTableName + " AS " + "select row_number() over (order by data asc) as id, "
subStringQuery = "SUBSTR(data,"
i = 1
query = crTable
finalQuery = " from " + sourceTableName

# Query snippet
print(query)
for key in dictionary:
    # i + "," + dictionary[key] + ") as " + key
    if (i == 1):
        subQuery = subStringQuery + str(i) + "," + dictionary[key] + ") as " + key + ","
        i = i + int(dictionary[key])
    else:
        subQuery = subStringQuery + str(i) + "," + dictionary[key] + ") as " + key + ","
        i = i + int(dictionary[key])
    print(subQuery)
print(finalQuery)
