// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Manager
 * @dev Program 095
 */
contract Program095 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Manager");
    }
}
