// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Hello World
 * @dev Program 001
 */
contract Program001 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Hello World");
    }
}
