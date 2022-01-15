
def transactionEntity(item) -> dict:
    """
    Gets an individual response from the API request and formats it to a dictionary.
    :param item: dict: API response
    :return: formatted data for API response
    """
    return{
        "_id": str(item["_id"]),
        "hash": item["hash"],
        "amount": item["amount"],
        "type": item["type"],
        "baseTransactions": item["baseTransactions"],
        "leftParentHash": item["leftParentHash"],
        "rightParentHash": item["rightParentHash"],
        "trustChainConsensus": item["trustChainConsensus"],
        "trustChainTrustScore": item["trustChainTrustScore"],
        "transactionConsensusUpdateTime": item["transactionConsensusUpdateTime"],
        "createTime": item["createTime"],
        "attachmentTime": item["attachmentTime"],
        "senderHash": item["senderHash"],
        "senderTrustScore": item["senderTrustScore"],
        "childrenTransactionHashes": item["childrenTransactionHashes"],
        "isValid": item["isValid"],
        "transactionDescription": item["transactionDescription"]
    }
def transactionsEntity(entity) -> list:
    """
    Gets a list of responses from an API query.
    :param entity: list: list of responses.
    :return: list of dictionaries containing each of the responses.
    """
    return [transactionEntity(item) for item in entity]