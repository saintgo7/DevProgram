// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Chainlink
 * @dev Program 050
 */
contract Program050 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Chainlink");
    }
}
