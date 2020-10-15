import requests


class PayeerAPI:
    def __init__(self, ACCOUNT, APIID, APIPASS):
        self.ACCOUNT = ACCOUNT
        self.APIID = APIID
        self.APIPASS = APIPASS


    """Request on Payeer API Server"""
    def __post_request(self, data):
        return requests.post('https://payeer.com/ajax/api/api.php', data=data).json()


    """-----------------------------------------------------------------------"""
    
    """The simplest query is checking authorization.
    It does not have to be fulfilled separately from primary actions.To check authorization,
    send a POST query to the URL https://payeer.com/ajax/api/api.php with three parameters: account, apiId и apiPass"""
    def check_authorization(self):
        data = {'account':self.ACCOUNT, 'apiId':self.APIID, 'apiPass':self.APIPASS}
        return self.__post_request(data)


    """You can check the existence of an account number prior to transfer in the Payeer system"""
    def check_existence_account_payeer(self, payeer_user):
        data = {'account':self.ACCOUNT, 'apiId':self.APIID, 'apiPass':self.APIPASS, 'action':'checkUser',  'user':payeer_user}
        return self.__post_request(data)


    """This method allows you to check the possibility of a payout without actually creating a payout
    (you can get the withdrawal/reception amount or check errors in parameters)"""
    def сheck_possibility_payout(self, payment_system_id, sum_incoming, currency_outgoing, currency_incoming, payment_account):
        data = {
        'account': self.ACCOUNT,
        'apiId': self.APIID, 
        'apiPass': self.APIPASS, 
        'action' : 'payoutChecking', 
        'ps' : payment_system_id,
        'sumout' : sum_incoming,
        'curIn' : currency_outgoing,
        'curOut' : currency_incoming,
        'param_ACCOUNT_NUMBER' : payment_account
        }
        return self.__post_request(data)
    
    """-----------------------------------------------------------------------"""
    
    """Getting a wallet balance"""
    def get_balance(self):
        data = {'account':self.ACCOUNT, 'apiId':self.APIID, 'apiPass':self.APIPASS, 'action':'getBalance'}
        return self.__post_request(data)


    """This method returns a list of payment systems that are available for payout"""
    def get_all_payment_system(self):
        data = {'account':self.ACCOUNT, 'apiId':self.APIID, 'apiPass':self.APIPASS, 'action':'getPaySystems'}
        return self.__post_request(data)


    """Get the history of account transactions"""
    def get_history_payment_operations(self):
        data = {'account':self.ACCOUNT, 'apiId':self.APIID, 'apiPass':self.APIPASS, 'action':'history'}
        return self.__post_request(data)
   
    """-----------------------------------------------------------------------"""


    """Transfer funds within the Payeer system"""
    def payout_inside_payeer(self, currency_outgoing, sum_outgoing, currency_incoming, payeer_account):
        data = {
        'account': self.ACCOUNT,
        'apiId': self.APIID, 
        'apiPass': self.APIPASS, 
        'action' : 'transfer', 
        'curIn' : currency_outgoing,
        'sum' : sum_outgoing,
        'curOut' : currency_incoming,
        'to' : payeer_account
        }
        return self.__post_request(data)


    """A payout to any payment system that supports Payeer"""
    def universal_payout(self, payment_system_id, sum_incoming, currency_outgoing, currency_incoming, payment_account):
        data = {
        'account': self.ACCOUNT,
        'apiId': self.APIID, 
        'apiPass': self.APIPASS, 
        'action' : 'payout', 
        'ps' : payment_system_id,
        'sumout' : sum_incoming,
        'curIn' : currency_outgoing,
        'curOut' : currency_incoming,
        'param_ACCOUNT_NUMBER' : payment_account
        }
        return self.__post_request(data)






