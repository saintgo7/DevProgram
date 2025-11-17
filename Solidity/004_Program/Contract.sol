// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Functions
 * @dev Program 004
 */
contract Program004 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Functions");
    }
}
