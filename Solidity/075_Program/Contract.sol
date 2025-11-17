// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Inline Assembly
 * @dev Program 075
 */
contract Program075 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Inline Assembly");
    }
}
