# Moccasin Project

🐍 Welcome to your Moccasin project!

## Deployment

1. Sepolia Contract Deployed Successfully - Contract Address: 0xE2CE98701bc87eF75F52039E4a048f26C570D97B
```bash
tx broadcasted: 0xee500ee7d8783a00c2bfdf1a361f78e98aba5010358141dcc668dd99f4f9ad36
/home/guire/.local/share/uv/python/cpython-3.12.7-linux-x86_64-gnu/lib/python3.12/functools.py:993: UserWarning: debug_traceTransaction not available! titanoboa will try hard to interact with the network, but this means that titanoboa is not able to do certain safety checks at runtime. it is recommended to switch to a node or provider with debug_traceTransaction.
  val = self.func(instance)
0xee500ee7d8783a00c2bfdf1a361f78e98aba5010358141dcc668dd99f4f9ad36 mined in block 0x66cbf5e8edd6ac9da27370d5d1b4d8e52ad8acd45dcd217c490bb2cc7b0d24ad!
contract deployed at 0xE2CE98701bc87eF75F52039E4a048f26C570D97B
The starting number is 7
tx broadcasted: 0x1e7d79e48992474ea209b8e32886a2f53a404208fe43799a0bdec7e0911f03e7
0x1e7d79e48992474ea209b8e32886a2f53a404208fe43799a0bdec7e0911f03e7 mined in block 0xb11a61854fac4202fb5fa6253bb00e34542e7eb648ca6094336b1e582a8eab36!
The ending number is 77
Smart-contract verification started
```

2. Sepolia-ZKSync Contract Deployed Successfully - Contract Address: 0xc5447Ab005f177aA484c00d3c8f362217Eb84FaE
```bash
guire@Anthony:~/vyper-course/mox-favorites-cu$ mox run deploy --network sepolia-zksync
Running run command...
The transactions run on this will actually be broadcast/transmitted, spending gas associated with your account. Are you sure you wish to continue?
Type 'y' or 'Y' and hit 'ENTER' or 'RETURN' to continue:
y
Enter your password for keystore Sepolia1: 
tx broadcasted: 0x3684d3552044da952f0976df2c5bba73117b740aca0e27005717dcf8650952b9
0x3684d3552044da952f0976df2c5bba73117b740aca0e27005717dcf8650952b9 mined in block 0x55cba3e96cfe94eecd3182b531a2bf467d3cee758101be1f73439bf18ed664bf!
Contract deployed at 0xc5447Ab005f177aA484c00d3c8f362217Eb84FaE
The starting number is 7
/home/guire/vyper-course/mox-favorites-cu/.venv/lib/python3.12/site-packages/boa/contracts/abi/abi_contract.py:127: UserWarning: No EIP-1559 transaction available, falling back to legacy
  computation = self.contract.env.execute_code(
/home/guire/vyper-course/mox-favorites-cu/.venv/lib/python3.12/site-packages/boa/contracts/abi/abi_contract.py:127: UserWarning: -32600: Unsupported method: eth_maxPriorityFeePerGas on zksync
  computation = self.contract.env.execute_code(
tx broadcasted: 0x4526a539961747529fd847b162a77e2c8176280cfd71f8420ce18da1580ea0b8
/home/guire/.local/share/uv/python/cpython-3.12.7-linux-x86_64-gnu/lib/python3.12/functools.py:993: UserWarning: debug_traceTransaction not available! titanoboa will try hard to interact with the network, but this means that titanoboa is not able to do certain safety checks at runtime. it is recommended to switch to a node or provider with debug_traceTransaction.
  val = self.func(instance)
0x4526a539961747529fd847b162a77e2c8176280cfd71f8420ce18da1580ea0b8 mined in block 0x6b99d36660e30f63a1fe4fd6badbb6da6e356ba3fe484c197580e013943dfbaf!
The ending number is 77
```

## Quickstart

```bash
mox init
mox run deploy
```

_For documentation, please run `mox --help` or visit [the Moccasin documentation](https://cyfrin.github.io/moccasin)_
