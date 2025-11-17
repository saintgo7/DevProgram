// Raycast
// Program 086

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program086.generated.h"

UCLASS()
class AProgram086 : public AActor
{
    GENERATED_BODY()

public:
    AProgram086();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
