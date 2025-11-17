// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title EIP Standards
 * @dev Program 086
 */
contract Program086 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("EIP Standards");
    }
}
