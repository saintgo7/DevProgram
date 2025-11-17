// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Fallback Function
 * @dev Program 009
 */
contract Program009 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Fallback Function");
    }
}
