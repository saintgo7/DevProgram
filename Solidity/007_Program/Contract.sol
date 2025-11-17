// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Payable
 * @dev Program 007
 */
contract Program007 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Payable");
    }
}
