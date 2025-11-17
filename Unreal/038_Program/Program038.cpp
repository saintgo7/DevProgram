// Blackboard

#include "Program038.h"

AProgram038::AProgram038()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram038::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Blackboard ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating blackboard."));

    // Implement the program logic here...
}

void AProgram038::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
