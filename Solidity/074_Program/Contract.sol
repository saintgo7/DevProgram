// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title View Pure
 * @dev Program 074
 */
contract Program074 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("View Pure");
    }
}
