// Client RPC

#include "Program094.h"

AProgram094::AProgram094()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram094::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Client RPC ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating client rpc."));

    // Implement the program logic here...
}

void AProgram094::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
