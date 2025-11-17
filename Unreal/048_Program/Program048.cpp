// User Widget

#include "Program048.h"

AProgram048::AProgram048()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram048::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== User Widget ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating user widget."));

    // Implement the program logic here...
}

void AProgram048::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
