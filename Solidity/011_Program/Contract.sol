// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title ERC20 Token
 * @dev Program 011
 */
contract Program011 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("ERC20 Token");
    }
}
