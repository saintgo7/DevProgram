// Replication
// Program 091

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program091.generated.h"

UCLASS()
class AProgram091 : public AActor
{
    GENERATED_BODY()

public:
    AProgram091();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
