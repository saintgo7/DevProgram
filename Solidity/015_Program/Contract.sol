// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title ICO
 * @dev Program 015
 */
contract Program015 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("ICO");
    }
}
