// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Random Number
 * @dev Program 076
 */
contract Program076 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Random Number");
    }
}
