from bitcoinlib.mnemonic import Mnemonic
from bitcoinlib.wallets import wallet_create_or_open as CO


def wallet():
    passphrase = Mnemonic().generate()
    print(passphrase)
    w = CO("Wallet2", keys=passphrase, network='bitcoin')
    account_btc2 = w.new_account('Account BTC')
    account_ltc1 = w.new_account('Account LTC', network='litecoin')
    print(w.get_key())
    print(w.get_key(account_btc2.account_id))
    print(w.get_key(account_ltc1.account_id))
    print(w.info())
    return '(Wallet Name: {0},\nCrypto Accounts: {1},\nBalance: {2})'.format(w.name, w.network_list(), w.balance())
