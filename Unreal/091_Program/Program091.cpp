// Replication

#include "Program091.h"

AProgram091::AProgram091()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram091::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Replication ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating replication."));

    // Implement the program logic here...
}

void AProgram091::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
