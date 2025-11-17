// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Modifiers
 * @dev Program 005
 */
contract Program005 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Modifiers");
    }
}
