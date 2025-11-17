// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title UUPS
 * @dev Program 064
 */
contract Program064 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("UUPS");
    }
}
