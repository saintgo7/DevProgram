// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Inheritance
 * @dev Program 025
 */
contract Program025 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Inheritance");
    }
}
