// Material Parameter

#include "Program068.h"

AProgram068::AProgram068()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram068::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Material Parameter ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating material parameter."));

    // Implement the program logic here...
}

void AProgram068::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
