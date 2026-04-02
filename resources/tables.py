import json

import pandas as pd

def parsingDate(date):
    if date == '0001-01-01':
        return None
    else:
        return date

class Tables:
    def salesOrders(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'number': e['number'],
                'orderDate': e['orderDate'],
                'postingDate': e['postingDate'],
                'yourReference': e['yourReference'],
                'customerNumber': e['customerNumber'],
                'customerName': e['customerName'],
                'billToCustomerNumber': e['billToCustomerNumber'],
                'shipToName': e['shipToName'],
                'shipmentMethodCode': e['shipmentMethodCode'],
                'requestedDeliveryDate': parsingDate(e['requestedDeliveryDate']),
                'discountAmount': e['discountAmount'],
                'totalAmountExcludingVAT': e['totalAmountExcludingVAT'],
                'totalAmountIncludingVAT': e['totalAmountIncludingVAT'],
                'fullyShipped': e['fullyShipped'],
                'status': e['status'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)

    def salesOrderLines(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'salesOrderNumber': e['salesOrderNumber'],
                'lineNumber': e['lineNumber'],
                'lineType': e['lineType'],
                'lineObjectNumber': e['lineObjectNumber'],
                'description': e['description'],
                'locationCode': e['locationCode'],
                'quantity': e['quantity'],
                'unitOfMeasureCode': e['unitOfMeasureCode'],
                'unitPrice': e['unitPrice'],
                'unitPricePer': e['unitPricePer'],
                'unitPriceUnitOfMeasureCode': e['unitPriceUnitOfMeasureCode'],
                'discountAmount': e['discountAmount'],
                'discountPercent': e['discountPercent'],
                'netAmount': e['netAmount'],
                'vatPercent': e['vatPercent'],
                'netAmountIncludingVAT': e['netAmountIncludingVAT'],
                'requestedDeliveryDate': parsingDate(e['requestedDeliveryDate']),
                'promisedDeliveryDate': parsingDate(e['promisedDeliveryDate']),
                'shipmentDate': parsingDate(e['shipmentDate']),
                'shipQuantity': e['shipQuantity'],
                'shippedQuantity': e['shippedQuantity'],
                'invoiceQuantity': e['invoiceQuantity'],
                'invoicedQuantity': e['invoicedQuantity'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)


    def salesInvoices(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'number': e['number'],
                'externalDocumentNumber': e['externalDocumentNumber'],
                'invoiceDate': parsingDate(e['invoiceDate']),
                'postingDate': parsingDate(e['postingDate']),
                'dueDate': parsingDate(e['dueDate']),
                'promisedPayDate': parsingDate(e['promisedPayDate']),
                'customerId': e['customerId'],
                'customerNumber': e['customerNumber'],
                'customerName': e['customerName'],
                'orderId': e['orderId'],
                'orderNumber': e['orderNumber'],
                'pricesIncludeTax': e['pricesIncludeTax'],
                'remainingAmount': e['remainingAmount'],
                'discountAmount': e['discountAmount'],
                'discountAppliedBeforeTax': e['discountAppliedBeforeTax'],
                'totalAmountExcludingTax': e['totalAmountExcludingTax'],
                'totalTaxAmount': e['totalTaxAmount'],
                'totalAmountIncludingTax': e['totalAmountIncludingTax'],
                'status': e['status'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)

    def itemCategories(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'code': e['code'],
                'displayName': e['displayName'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)

    def locations(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'code': e['code'],
                'displayName': e['displayName'],
                'addressLine1': e['addressLine1'],
                'city': e['city'],
                'country': e['country'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)

    def customers(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'name': e['name'],
                'city': e['city'],
                'countryRegionCode': e['countryRegionCode'],
                'customerPostingGroup': e['customerPostingGroup'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)

    def employees(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'number': e['number'],
                'resourceNumber': e['resourceNumber'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)

    def generalLedgerEntries(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'entryNumber': e['entryNumber'],
                'postingDate': parsingDate(e['postingDate']),
                'documentNumber': e['documentNumber'],
                'documentType': e['documentType'],
                'accountNumber': e['accountNumber'],
                'description': e['description'],
                'debitAmount': e['debitAmount'],
                'creditAmount': e['creditAmount'],
                'additionalCurrencyDebitAmount': e['additionalCurrencyDebitAmount'],
                'additionalCurrencyCreditAmount': e['additionalCurrencyCreditAmount'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)

    def itemCalculationProdBomLines(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'parentType': e['parentType'],
                'lineQuantity': e['lineQuantity'],
                'level': e['level'],
                'lineNumber': e['lineNumber'],
                'itemNumber': e['itemNumber'],
                'description': e['description'],
                'quantityPiece': e['quantityPiece'],
                'baseUnitOfMeasureCode': e['baseUnitOfMeasureCode'],
                'quantityPer': e['quantityPer'],
                'quantity': e['quantity'],
                'totalQuantity': e['totalQuantity'],
                'unitCostPrice': e['unitCostPrice'],
                'quantityPerCostPriceDimension': e['quantityPerCostPriceDimension'],
                'costPriceUnitOfMeasureCode': e['costPriceUnitOfMeasureCode'],
                'costPriceDiscountAmount': e['costPriceDiscountAmount'],
                'totalCostPrice': e['totalCostPrice'],
                'markupAmount': e['markupAmount'],
                'unitSalesPrice': e['unitSalesPrice'],
                'quantityPerSalesPriceDimension': e['quantityPerSalesPriceDimension'],
                'salesDiscountAmount': e['salesDiscountAmount'],
                'totalSalesPrice': e['totalSalesPrice'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)



    def itemCalculationRoutingLines(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'itemNumber': e['itemNumber'],
                'totalQuantity': e['totalQuantity'],
                'level': e['level'],
                'description': e['description'],
                'workCenterGroupCode': e['workCenterGroupCode'],
                'workCenterNumber': e['workCenterNumber'],
                'unitCostCalculation': e['unitCostCalculation'],
                'isSubcontracting': e['isSubcontracting'],
                'baseSetupTime': e['baseSetupTime'],
                'setupTimeUnitOfMeasureCode': e['setupTimeUnitOfMeasureCode'],
                'baseRunTime': e['baseRunTime'],
                'runTimeUnitOfMeasureCode': e['runTimeUnitOfMeasureCode'],
                'baseTotalRunTime': e['baseTotalRunTime'],
                'baseTotalTime': e['baseTotalTime'],
                'baseCostPerUnitOfMeasure': e['baseCostPerUnitOfMeasure'],
                'totalBaseSetupCost': e['totalBaseSetupCost'],
                'totalBaseRunCost': e['totalBaseRunCost'],
                'totalBaseCost': e['totalBaseCost'],
                'employeeCostGroupNumber': e['employeeCostGroupNumber'],
                'employeeSetupTime': e['employeeSetupTime'],
                'employeeRunTime': e['employeeRunTime'],
                'employeeTotalRunTime': e['employeeTotalRunTime'],
                'employeeTotalTime': e['employeeTotalTime'],
                'employeeCostPerUnitOfMeasure': e['employeeCostPerUnitOfMeasure'],
                'totalEmployeeSetupCost': e['totalEmpolyeeSetupCost'],
                'totalEmployeeRunCost': e['totalEmployeeRunCost'],
                'totalEmployeeCost': e['totalEmployeeCost'],
                'totalSetupCost': e['totalSetupCost'],
                'totalRunCost': e['totalRunCost'],
                'totalCostPrice': e['totalCostPrice'],
                'costPriceUnitOfMeasureCode': e['costPriceUnitOfMeasureCode'],
                'markupAmount': e['markupAmount'],
                'totalSalesPrice': e['totalSalesPrice'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)

    def itemCalculations(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'number': e['number'],
                'date': parsingDate(e['date']),
                'itemNumber': e['itemNumber'],
                'quantity': e['quantity'],
                'sourceLineNumber': e['sourceLineNumber'],
                'postedSalesInvoiceNumber': e['postedSalesInvoiceNumber'],
                'postedSalesInvoiceLineNumber': e['postedSalesInvoiceLineNumber'],
                'costPricePerPiece': e['costPricePerPiece'],
                'totalCostPrice': e['totalCostPrice'],
                'salesPricePerPiece': e['salesPricePerPiece'],
                'totalSalesPrice': e['totalSalesPrice'],
                'calculationState': e['calculationState'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)
    
    def itemVariants(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)

    def items(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'number': e['number'],
                'description': e['description'],
                'baseUnitOfMeasureCode': e['baseUnitOfMeasureCode'],
                'type': e['type'],
                'blocked': e['blocked'],
                'productionBillOfMaterialNumber': e['productionBillOfMaterialNumber'],
                'routingNumber': e['routingNumber'],
                'inventoryPostingGroup': e['inventoryPostingGroup'],
                'unitCost': e['unitCost'],
                'unitPrice': e['unitPrice'],
                'vendorNumber': e['vendorNumber'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)

    def productionBOMHeaders(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'number': e['number'],
                'description': e['description'],
                'unitOfMeasureCode': e['unitOfMeasureCode'],
                'status': e['status'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)

    def productionBOMLines(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'productionBillOfMaterialNumber': e['productionBillOfMaterialNumber'],
                'lineNumber': e['lineNumber'],
                'type': e['type'],
                'quantityPiece': e['quantityPiece'],
                'quantityPer': e['quantityPer'],
                'quantity': e['quantity'],
                'unitOfMeasureCode': e['unitOfMeasureCode'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)

    def productionOrders(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'status': e['status'],
                'number': e['number'],
                'locationCode': e['locationCode'],
                'description': e['description'],
                'startingDateTime': pd.to_datetime(e['startingDateTime']),
                'endingDateTime': pd.to_datetime(e['endingDateTime']),
                'dueDate': parsingDate(e['dueDate']),
                'productionStatus': e['productionStatus'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)

    def purchaseCreditMemos(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'number': e['number'],
                'creditMemoDate': parsingDate(e['creditMemoDate']),
                'postingDate': parsingDate(e['postingDate']),
                'dueDate': parsingDate(e['dueDate']),
                'vendorId': e['vendorId'],
                'vendorNumber': e['vendorNumber'],
                'vendorName': e['vendorName'],
                'currencyCode': e['currencyCode'],
                'discountAmount': e['discountAmount'],
                'totalAmountExcludingTax': e['totalAmountExcludingTax'],
                'totalTaxAmount': e['totalTaxAmount'],
                'totalAmountIncludingTax': e['totalAmountIncludingTax'],
                'status': e['status'],
                'invoiceNumber': e['invoiceNumber'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)

    def purchaseInvoices(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'number': e['number'],
                'postingDate': parsingDate(e['postingDate']),
                'invoiceDate': parsingDate(e['invoiceDate']),
                'dueDate': parsingDate(e['dueDate']),
                'vendorInvoiceNumber': e['vendorInvoiceNumber'],
                'vendorId': e['vendorId'],
                'vendorName': e['vendorName'],
                'currencyCode': e['currencyCode'],
                'discountAmount': e['discountAmount'],
                'totalAmountExcludingTax': e['totalAmountExcludingTax'],
                'totalTaxAmount': e['totalTaxAmount'],
                'totalAmountIncludingTax': e['totalAmountIncludingTax'],
                'status': e['status'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)

    def purchaseOrders(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'number': e['number'],
                'orderDate': parsingDate(e['orderDate']),
                'postingDate': parsingDate(e['postingDate']),
                'vendorId': e['vendorId'],
                'vendorNumber': e['vendorNumber'],
                'vendorName': e['vendorName'],
                'requestedReceiptDate': parsingDate(e['requestedReceiptDate']),
                'currencyCode': e['currencyCode'],
                'discountAmount': e['discountAmount'],
                'totalAmountExcludingTax': e['totalAmountExcludingTax'],
                'totalTaxAmount': e['totalTaxAmount'],
                'totalAmountIncludingTax': e['totalAmountIncludingTax'],
                'fullyReceived': e['fullyReceived'],
                'status': e['status'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)

    def routingHeaders(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'number': e['number'],
                'description': e['description'],
                'type': e['type'],
                'status': e['status'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)

    def routingLines(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'routingNumber': e['routingNumber'],
                'description': e['description'],
                'useEmployeeTimePercentage': e['useEmployeeTimePercentage'],
                'employeeTimePercentage': e['employeeTimePercentage'],
                'setupTime': e['setupTime'],
                'setupTimeEmployee': e['setupTimeEmployee'],
                'setupTimeUnitOfMeasureCode': e['setupTimeUnitOfMeasureCode'],
                'runTime': e['runTime'],
                'runTimeEmployee': e['runTimeEmployee'],
                'runTimeUnitOfMeasureCode': e['runTimeUnitOfMeasureCode'],
                'waitTime': e['waitTime'],
                'waitTimeUnitOfMeasureCode': e['waitTimeUnitOfMeasureCode'],
                'moveTime': e['moveTime'],
                'moveTimeUnitOfMeasureCode': e['moveTimeUnitOfMeasureCode'],
                'routingLinkCode': e['routingLinkCode'],
                'lotSize': e['lotSize'],
                'sendAheadQuantity': e['sendAheadQuantity'],
                'concurrentCapacities': e['concurrentCapacities'],
                'scrapFactorPercentage': e['scrapFactorPercentage'],
                'fixedScrapQuantity': e['fixedScrapQuantity'],
                'unitCostPer': e['unitCostPer'],
                'subcontractingVendorNumber': e['subcontractingVendorNumber'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)

    def salesCreditMemos(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'number': e['number'],
                'externalDocumentNumber': e['externalDocumentNumber'],
                'creditMemoDate': parsingDate(e['creditMemoDate']),
                'postingDate': parsingDate(e['postingDate']),
                'dueDate': parsingDate(e['dueDate']),
                'customerId': e['customerId'],
                'customerNumber': e['customerNumber'],
                'customerName': e['customerName'],
                'currencyCode': e['currencyCode'],
                'discountAmount': e['discountAmount'],
                'totalAmountExcludingTax': e['totalAmountExcludingTax'],
                'totalTaxAmount': e['totalTaxAmount'],
                'totalAmountIncludingTax': e['totalAmountIncludingTax'],
                'status': e['status'],
                'invoiceId': e['invoiceId'],
                'invoiceNumber': e['invoiceNumber'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)

    def salesShipments(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'number': e['number'],
                'externalDocumentNumber': e['externalDocumentNumber'],
                'invoiceDate': parsingDate(e['invoiceDate']),
                'postingDate': parsingDate(e['postingDate']),
                'dueDate': parsingDate(e['dueDate']),
                'customerPurchaseOrderReference': e['customerPurchaseOrderReference'],
                'customerId': e['customerId'],
                'customerNumber': e['customerNumber'],
                'customerName': e['customerName'],
                'currencyCode': e['currencyCode'],
                'orderNumber': e['orderNumber'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)

    def salesShipmentLines(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'documentId': e['documentId'],
                'documentNo': e['documentNo'],
                'sequence': e['sequence'],
                'lineObjectNumber': e['lineObjectNumber'],
                'description': e['description'],
                'unitOfMeasureCode': e['unitOfMeasureCode'],
                'unitPrice': e['unitPrice'],
                'quantity': e['quantity'],
                'discountPercent': e['discountPercent'],
                'taxPercent': e['taxPercent'],
                'shipmentDate': parsingDate(e['shipmentDate'])
            })
        return pd.DataFrame(data)

    def vendors(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'number': e['number'],
                'displayName': e['displayName'],
                'city': e['city'],
                'country': e['country'],
                'taxLiable': e['taxLiable'],
                'balance': e['balance'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)

    def workCenters(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'number': e['number'],
                'name': e['name'],
                'workCenterGroupCode': e['workCenterGroupCode'],
                'shopCalendarCode': e['shopCalendarCode'],
                'locationCode': e['locationCode'],
                'blocked': e['blocked'],
                'flushingMethod': e['flushingMethod'],
                'unitCostCalculation': e['unitCostCalculation'],
                "useEmployeeTimePercentage": e["useEmployeeTimePercentage"],
                "defaultEmployeeTimePercentage": e["defaultEmployeeTimePercentage"],
                "workCenterCost": e["workCenterCost"],
                "overheadRate": e["overheadRate"],
                "indirectCostPercentage": e["indirectCostPercentage"],
                "defaultEmployeeCost": e["defaultEmployeeCost"],
                "directUnitCost": e["directUnitCost"],
                "unitCost": e["unitCost"],
                "unitOfMeasureCode": e["unitOfMeasureCode"],
                "specificUnitCost": e["specificUnitCost"],
                "subcontractorNumber": e["subcontractorNumber"],
                "efficiency": e["efficiency"],
                "defaultRoutingLinkCode": e["defaultRoutingLinkCode"],
                "queueTime": e["queueTime"],
                "queueTimeUnitOfMeasureCode": e["queueTimeUnitOfMeasureCode"],
                "setupTime": e["setupTime"],
                "setupTimeUnitOfMeasureCode": e["setupTimeUnitOfMeasureCode"],
                "runTimeUnitOfMeasureCode": e["runTimeUnitOfMeasureCode"],
                "waitTime": e["waitTime"],
                "waitTimeUnitOfMeasureCode": e["waitTimeUnitOfMeasureCode"],
                "moveTime": e["moveTime"],
                "moveTimeUnitOfMeasureCode": e["moveTimeUnitOfMeasureCode"],
                "preferencePriority": e["preferencePriority"],
                "blockedForRouting": e["blockedForRouting"],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)

    def accounts(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'number': e['number'],
                'displayName': e['displayName'],
                'category': e['category'],
                'subCategory': e['subCategory'],
                'blocked': e['blocked'],
                'accountType': e['accountType'],
                'directPosting': e['directPosting'],
                'netChange': e['netChange'],
                'consolidationTranslationMethod': e['consolidationTranslationMethod'],
                'consolidationDebitAccount': e['consolidationDebitAccount'],
                'consolidationCreditAccount': e['consolidationCreditAccount'],
                'excludeFromConsolidation': e['excludeFromConsolidation'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)


    def jobQueueEntries(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'userId': e['userId'],
                'lastReadyState': pd.to_datetime(e['lastReadyState']),
                'objectCaptionToRun': e['objectCaptionToRun'],
                'earliestStartDateTime': pd.to_datetime(e['earliestStartDateTime']),
                'status': e['status'],
                'recurringJob': e['recurringJob'],
                'description': e['description'],
                'errorMessage': e['errorMessage'],
                'scheduled': e['scheduled'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)


    def purchaseInvoiceLines(resp):
        data = []
        for e in resp:
            for l in e['purchaseInvoiceLines']:
                data.append({
                    'purchaseInvoiceId': e['id'],
                    'id': l['id'],
                    'sequence': l['sequence'],
                    'lineType': l['lineType'],
                    'lineObjectNumber': l['lineObjectNumber'],
                    'description': l['description'],
                    'unitCost': l['unitCost'],
                    'quantity': l['quantity'],
                    'discountAmount': l['discountAmount'],
                    'netAmount': l['netAmount'],
                    'netTaxAmount': l['netTaxAmount'],
                    'netAmountIncludingTax': l['netAmountIncludingTax'],
                    'expectedReceiptDate': l['expectedReceiptDate'],
                    'locationId': l['locationId'],
                    'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
                })
        return pd.DataFrame(data)

    def purchaseCreditMemoLines(resp):
        data = []
        for e in resp:
            for l in e['purchaseCreditMemoLines']:
                data.append({
                    'purchaseCreditMemoId': e['id'],
                    'id': l['id'],
                    'sequence': l['sequence'],
                    'lineType': l['lineType'],
                    'accountId': l['accountId'],
                    'lineObjectNumber': l['lineObjectNumber'],
                    'description': l['description'],
                    'unitCost': l['unitCost'],
                    'quantity': l['quantity'],
                    'discountAmount': l['discountAmount'],
                    'netAmount': l['netAmount'],
                    'netTaxAmount': l['netTaxAmount'],
                    'netAmountIncludingTax': l['netAmountIncludingTax'],
                    'locationId': l['locationId'],
                    'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
                })
        return pd.DataFrame(data)

    def purchaseOrderLines(resp):
        data = []
        for e in resp:
            for l in e['purchaseOrderLines']:
                data.append({
                    'purchaseOrderId': e['id'],
                    'id': l['id'],
                    'itemid': l['itemId'],
                    'sequence': l['sequence'],
                    'lineType': l['lineType'],
                    'accountId': l['accountId'],
                    'lineObjectNumber': l['lineObjectNumber'],
                    'description': l['description'],
                    'directUnitCost': l['directUnitCost'],
                    'quantity': l['quantity'],
                    'discountAmount': l['discountAmount'],
                    'netAmount': l['netAmount'],
                    'netTaxAmount': l['netTaxAmount'],
                    'netAmountIncludingTax': l['netAmountIncludingTax'],
                    'expectedReceiptDate': l['expectedReceiptDate'],
                    'receivedQuantity': l['receivedQuantity'],
                    'receiveQuantity': l['receiveQuantity'],
                    'locationId': l['locationId'],
                    'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
                })
        return pd.DataFrame(data)

    def salesInvoiceLines(resp):
        data = []
        for e in resp:
            for l in e['salesInvoiceLines']:
                data.append({
                    'salesInvoiceId': e['id'],
                    'id': l['id'],
                    'itemid': l['itemId'],
                    'sequence': l['sequence'],
                    'lineType': l['lineType'],
                    'accountId': l['accountId'],
                    'lineObjectNumber': l['lineObjectNumber'],
                    'description': l['description'],
                    'unitPrice': l['unitPrice'],
                    'quantity': l['quantity'],
                    'discountAmount': l['discountAmount'],
                    'netAmount': l['netAmount'],
                    'netTaxAmount': l['netTaxAmount'],
                    'netAmountIncludingTax': l['netAmountIncludingTax'],
                    'shipmentDate': l['shipmentDate'],
                    'locationId': l['locationId'],
                    'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
                })
        return pd.DataFrame(data)

    def salesCreditMemoLines(resp):
        data = []
        for e in resp:
            for l in e['salesCreditMemoLines']:
                data.append({
                    'salesCreditMemoId': e['id'],
                    'id': l['id'],
                    'sequence': l['sequence'],
                    'lineType': l['lineType'],
                    'accountId': l['accountId'],
                    'lineObjectNumber': l['lineObjectNumber'],
                    'description': l['description'],
                    'unitPrice': l['unitPrice'],
                    'quantity': l['quantity'],
                    'discountAmount': l['discountAmount'],
                    'netAmount': l['netAmount'],
                    'netTaxAmount': l['netTaxAmount'],
                    'netAmountIncludingTax': l['netAmountIncludingTax'],
                    'locationId': l['locationId'],
                    'shipmentDate': l['shipmentDate'],
                    'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
                })
        return pd.DataFrame(data)

    def projects(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'number': e['number'],
                'displayName': e['displayName'],
                'type': e['type'],
                'city': e['city'],
                'country': e['country'],
                'taxLiable': e['taxLiable'],
                'balanceDue': e['balanceDue'],
                'creditLimit': e['creditLimit'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)

    def userPermissions(resp):
        data = []
        for e in resp:
            for l in e['userPermissions']:
                data.append({
                    'id': l['id'],
                    'userSecurityId': e['userSecurityId'],
                    'userName': e['userName'],
                    'userDisplayName': e['displayName'],
                    'state': e['state'],
                    'contactEmail': e['contactEmail'],
                    'roleId': l['roleId'],
                    'roleDisplayName': l['displayName'],
                    'company': l['company'],
                    'appId': l['appId'],
                    'extensionName': l['extensionName'],
                    'scope': l['scope'],
                })
        return pd.DataFrame(data)


    def sample(resp):
        data = []
        for e in resp:
            data.append({
                'id': e['id'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)


    def check(resp):
        data = []

        if 1 == 1:
            with open('kaas.json', 'w', encoding='utf-8') as f:
                json.dump(resp[:10], f, indent=4, ensure_ascii=False)
            exit()

        for e in resp:
            data.append({
                'id': e['id'],
                'lastModifiedDateTime': pd.to_datetime(e['lastModifiedDateTime'])
            })
        return pd.DataFrame(data)
