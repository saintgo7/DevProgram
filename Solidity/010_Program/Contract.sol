// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Receive Function
 * @dev Program 010
 */
contract Program010 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Receive Function");
    }
}
