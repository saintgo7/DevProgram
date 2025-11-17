// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Upgradeable Contract
 * @dev Program 061
 */
contract Program061 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Upgradeable Contract");
    }
}
