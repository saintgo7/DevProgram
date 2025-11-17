// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Abstract Contract
 * @dev Program 024
 */
contract Program024 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Abstract Contract");
    }
}
