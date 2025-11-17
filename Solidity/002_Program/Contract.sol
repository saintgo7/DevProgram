// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Basic Contract
 * @dev Program 002
 */
contract Program002 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Basic Contract");
    }
}
