// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Access Control
 * @dev Program 017
 */
contract Program017 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Access Control");
    }
}
