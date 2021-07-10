import asyncio

from blspy import G2Element
from clvm_tools import binutils

from kale.consensus.block_rewards import calculate_base_farmer_reward, calculate_pool_reward
from kale.rpc.full_node_rpc_client import FullNodeRpcClient
from kale.types.blockchain_format.program import Program
from kale.types.coin_solution import CoinSolution
from kale.types.spend_bundle import SpendBundle
from kale.util.bech32m import decode_puzzle_hash
from kale.util.config import load_config
from kale.util.default_root import DEFAULT_ROOT_PATH
from kale.util.ints import uint32, uint16


async def main() -> None:
    rpc_port: uint16 = uint16(6355)
    self_hostname = "localhost"
    path = DEFAULT_ROOT_PATH
    config = load_config(path, "config.yaml")
    client = await FullNodeRpcClient.create(self_hostname, rpc_port, path, config)
    try:
        farmer_prefarm = (await client.get_block_record_by_height(1)).reward_claims_incorporated[1]
        pool_prefarm = (await client.get_block_record_by_height(1)).reward_claims_incorporated[0]

        pool_amounts = int(calculate_pool_reward(uint32(0)) / 2)
        farmer_amounts = int(calculate_base_farmer_reward(uint32(0)) / 2)
        print(farmer_prefarm.amount, farmer_amounts)
        assert farmer_amounts == farmer_prefarm.amount // 2
        assert pool_amounts == pool_prefarm.amount // 2
        address1 = "xka1vshypxxd3hgkzaqcdqrqhk8sa2at3h97d6vyck3vfwcq56wvjmfqv8h8kd"  # Key 1
        address2 = "xka1vshypxxd3hgkzaqcdqrqhk8sa2at3h97d6vyck3vfwcq56wvjmfqv8h8kd"  # Key 2

        ph1 = decode_puzzle_hash(address1)
        ph2 = decode_puzzle_hash(address2)

        p_farmer_2 = Program.to(
            binutils.assemble(f"(q . ((51 0x{ph1.hex()} {farmer_amounts}) (51 0x{ph2.hex()} {farmer_amounts})))")
        )
        p_pool_2 = Program.to(
            binutils.assemble(f"(q . ((51 0x{ph1.hex()} {pool_amounts}) (51 0x{ph2.hex()} {pool_amounts})))")
        )

        p_solution = Program.to(binutils.assemble("()"))

        sb_farmer = SpendBundle([CoinSolution(farmer_prefarm, p_farmer_2, p_solution)], G2Element())
        sb_pool = SpendBundle([CoinSolution(pool_prefarm, p_pool_2, p_solution)], G2Element())

        print(sb_pool, sb_farmer)
        res = await client.push_tx(sb_farmer)
        # res = await client.push_tx(sb_pool)

        print(res)
        up = await client.get_coin_records_by_puzzle_hash(farmer_prefarm.puzzle_hash, True)
        uf = await client.get_coin_records_by_puzzle_hash(pool_prefarm.puzzle_hash, True)
        print(up)
        print(uf)
    finally:
        client.close()


asyncio.run(main())
