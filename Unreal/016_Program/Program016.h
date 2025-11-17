// UObject
// Program 016

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program016.generated.h"

UCLASS()
class AProgram016 : public AActor
{
    GENERATED_BODY()

public:
    AProgram016();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
