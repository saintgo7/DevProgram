// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Cross Chain
 * @dev Program 081
 */
contract Program081 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Cross Chain");
    }
}
