// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Transfer Ether
 * @dev Program 008
 */
contract Program008 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Transfer Ether");
    }
}
