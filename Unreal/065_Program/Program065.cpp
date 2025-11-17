// Physics Constraint

#include "Program065.h"

AProgram065::AProgram065()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram065::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Physics Constraint ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating physics constraint."));

    // Implement the program logic here...
}

void AProgram065::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
