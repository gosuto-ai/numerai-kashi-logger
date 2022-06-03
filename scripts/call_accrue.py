from brownie import Contract, accounts


def main():
    nmrusdc = Contract(
        '0x7BEe2161AfA1aEe4466E77BED826a41D5A28DB46', owner=accounts[0]
    )
    tx = nmrusdc.accrue()
    rate_bps = round(tx.events['LogAccrue']['rate'] / 365 / 24 / 60 / 60 / 1000, 4)
    util = round(tx.events['LogAccrue']['utilization'] / 1e18 * 100, 4)
    print('nmrusdc')
    print('current rate:', rate_bps)
    print('current util:', util)

    nmrweth = Contract(
        '0x273BEE1589037aF28E37955304eB92870e503B2f', owner=accounts[0]
    )
    tx = nmrweth.accrue()
    rate_bps = round(tx.events['LogAccrue']['rate'] / 365 / 24 / 60 / 60 / 1000, 4)
    util = round(tx.events['LogAccrue']['utilization'] / 1e18 * 100, 4)
    print('nmrweth')
    print('current rate:', rate_bps)
    print('current util:', util)
