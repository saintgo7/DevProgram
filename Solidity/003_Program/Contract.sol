// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title State Variables
 * @dev Program 003
 */
contract Program003 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("State Variables");
    }
}
