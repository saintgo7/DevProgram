// Overlap
// Program 089

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program089.generated.h"

UCLASS()
class AProgram089 : public AActor
{
    GENERATED_BODY()

public:
    AProgram089();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
