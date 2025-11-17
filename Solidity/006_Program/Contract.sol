// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Constructor
 * @dev Program 006
 */
contract Program006 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Constructor");
    }
}
