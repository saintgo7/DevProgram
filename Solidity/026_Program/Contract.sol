// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Events
 * @dev Program 026
 */
contract Program026 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Events");
    }
}
